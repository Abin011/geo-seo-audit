# -*- coding: utf-8 -*-
"""页面抓取与站点发现。"""

from __future__ import annotations

import json
import re
import time
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

AI_CRAWLERS = [
    "GPTBot", "ChatGPT-User", "OAI-SearchBot", "ClaudeBot", "anthropic-ai",
    "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot-Extended",
    "CCBot", "Bytespider", "Meta-ExternalAgent", "FacebookBot", "Amazonbot",
    "cohere-ai", "Bingbot", "Googlebot",
]


def normalize_url(url: str) -> str:
    url = url.strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}/"


def fetch_url(url: str, timeout: int = 30) -> tuple[requests.Response | None, float, str | None]:
    """返回 (response, 耗时秒, 错误信息)。"""
    t0 = time.perf_counter()
    try:
        resp = requests.get(
            url, headers=DEFAULT_HEADERS, timeout=timeout, allow_redirects=True
        )
        return resp, time.perf_counter() - t0, None
    except requests.RequestException as e:
        return None, time.perf_counter() - t0, str(e)


def parse_page(html: str, url: str) -> dict:
    soup = BeautifulSoup(html, "lxml")
    title_tag = soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else None

    meta_desc = None
    robots_meta = None
    og_title = None
    for meta in soup.find_all("meta"):
        name = (meta.get("name") or meta.get("property") or "").lower()
        content = meta.get("content") or ""
        if name == "description":
            meta_desc = content
        if name == "robots":
            robots_meta = content
        if name == "og:title":
            og_title = content

    canonical_tag = soup.find("link", rel="canonical")
    canonical = canonical_tag.get("href") if canonical_tag else None

    h1s, h2s = [], []
    for level in (1, 2):
        for h in soup.find_all(f"h{level}"):
            text = h.get_text(strip=True)
            if level == 1:
                h1s.append(text)
            else:
                h2s.append(text)

    schema_types: set[str] = set()
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string or "")
            graphs = data if isinstance(data, list) else [data]
            if isinstance(data, dict) and "@graph" in data:
                graphs = data["@graph"]
            for item in graphs:
                if isinstance(item, dict) and "@type" in item:
                    t = item["@type"]
                    if isinstance(t, list):
                        schema_types.update(t)
                    else:
                        schema_types.add(t)
        except (json.JSONDecodeError, TypeError):
            pass

    hreflangs = [
        (link.get("hreflang"), link.get("href"))
        for link in soup.find_all("link", rel="alternate")
        if link.get("hreflang")
    ]

    imgs = soup.find_all("img")
    img_total = len(imgs)
    img_no_alt = sum(1 for i in imgs if not i.get("alt"))
    img_empty_alt = sum(1 for i in imgs if i.get("alt") == "")

    body = BeautifulSoup(html, "lxml")
    for tag in body.find_all(["script", "style"]):
        tag.decompose()
    text = body.get_text(separator=" ", strip=True)
    word_count = len(text.split())

    js_count = len(soup.find_all("script", src=True))
    css_count = len(
        soup.find_all("link", rel=lambda x: x and "stylesheet" in x)
    )

    parsed = urlparse(url)
    internal = []
    for a in soup.find_all("a", href=True):
        href = urljoin(url, a["href"])
        if urlparse(href).netloc == parsed.netloc:
            internal.append(href)

    return {
        "url": url,
        "title": title,
        "title_len": len(title) if title else 0,
        "meta_description": meta_desc,
        "meta_desc_len": len(meta_desc) if meta_desc else 0,
        "robots_meta": robots_meta,
        "og_title": og_title,
        "canonical": canonical,
        "h1": h1s,
        "h2_count": len(h2s),
        "h2_sample": h2s[:8],
        "schema_types": sorted(schema_types),
        "hreflang": hreflangs,
        "word_count": word_count,
        "img_total": img_total,
        "img_no_alt": img_no_alt,
        "img_empty_alt": img_empty_alt,
        "js_external": js_count,
        "css_external": css_count,
        "internal_link_count": len(set(internal)),
        "has_faq_keyword": bool(
            re.search(r"faq|常见问题|frequently asked", html, re.I)
        ),
    }


def fetch_robots(base_url: str, timeout: int = 15) -> dict:
    parsed = urlparse(base_url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
    result = {
        "url": robots_url,
        "exists": False,
        "content": "",
        "sitemaps": [],
        "duplicate_user_agent": False,
        "ai_crawler_status": {},
        "errors": [],
    }
    resp, _, err = fetch_url(robots_url, timeout)
    if err:
        result["errors"].append(err)
        return result
    if resp.status_code != 200:
        result["errors"].append(f"HTTP {resp.status_code}")
        return result

    result["exists"] = True
    result["content"] = resp.text
    ua_count = len(re.findall(r"(?i)^user-agent:", resp.text, re.M))
    result["duplicate_user_agent"] = ua_count > 2

    for line in resp.text.splitlines():
        if line.lower().startswith("sitemap:"):
            result["sitemaps"].append(line.split(":", 1)[1].strip())

    lines = resp.text.splitlines()
    agents: dict[str, list] = {}
    current = None
    for line in lines:
        s = line.strip()
        if s.lower().startswith("user-agent:"):
            current = s.split(":", 1)[1].strip()
            agents.setdefault(current, [])
        elif current and s.lower().startswith("disallow:"):
            agents[current].append(("disallow", s.split(":", 1)[1].strip()))
        elif current and s.lower().startswith("allow:"):
            agents[current].append(("allow", s.split(":", 1)[1].strip()))

    for crawler in AI_CRAWLERS:
        if crawler in agents:
            rules = agents[crawler]
            if any(d == "/" for _, d in rules if _ == "disallow"):
                result["ai_crawler_status"][crawler] = "blocked"
            elif any(_ == "disallow" for _ in rules):
                result["ai_crawler_status"][crawler] = "partial"
            else:
                result["ai_crawler_status"][crawler] = "allowed"
        elif "*" in agents:
            wild = agents["*"]
            if any(d == "/" for _, d in wild if _ == "disallow"):
                result["ai_crawler_status"][crawler] = "blocked_wildcard"
            else:
                result["ai_crawler_status"][crawler] = "implicit_allow"
        else:
            result["ai_crawler_status"][crawler] = "implicit_allow"

    return result


def fetch_llms(base_url: str, timeout: int = 15) -> dict:
    parsed = urlparse(base_url)
    llms_url = f"{parsed.scheme}://{parsed.netloc}/llms.txt"
    out = {"url": llms_url, "exists": False, "size": 0, "has_chinese": False, "line_count": 0}
    resp, _, _ = fetch_url(llms_url, timeout)
    if resp and resp.status_code == 200:
        out["exists"] = True
        out["size"] = len(resp.content)
        out["line_count"] = resp.text.count("\n") + 1
        out["has_chinese"] = bool(re.search(r"[\u4e00-\u9fff]", resp.text))
        out["preview"] = resp.text[:500]
    return out


def crawl_sitemap(base_url: str, max_urls: int = 50, timeout: int = 20) -> list[str]:
    parsed = urlparse(base_url)
    candidates = [
        f"{parsed.scheme}://{parsed.netloc}/sitemap_index.xml",
        f"{parsed.scheme}://{parsed.netloc}/sitemap.xml",
        f"{parsed.scheme}://{parsed.netloc}/wp-sitemap.xml",
    ]
    found: set[str] = set()

    def parse_xml(text: str) -> list[str]:
        soup = BeautifulSoup(text, "lxml-xml")
        urls = []
        for loc in soup.find_all("loc"):
            if loc.string:
                urls.append(loc.string.strip())
        return urls

    for sm_url in candidates:
        resp, _, _ = fetch_url(sm_url, timeout)
        if not resp or resp.status_code != 200:
            continue
        locs = parse_xml(resp.text)
        for loc in locs:
            if loc.endswith(".xml"):
                child, _, _ = fetch_url(loc, timeout)
                if child and child.status_code == 200:
                    for u in parse_xml(child.text):
                        found.add(u)
                        if len(found) >= max_urls:
                            return list(found)[:max_urls]
            else:
                found.add(loc)
            if len(found) >= max_urls:
                return list(found)[:max_urls]
        if found:
            break

    return list(found)[:max_urls]
