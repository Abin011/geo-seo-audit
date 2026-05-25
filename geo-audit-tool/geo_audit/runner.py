# -*- coding: utf-8 -*-
"""审计流程编排。"""

from __future__ import annotations

import sys
from urllib.parse import urlparse

from geo_audit.analyzers import (
    AuditResult,
    Issue,
    compute_scores,
    detect_duplicate_products,
    guess_industry,
)
from geo_audit.fetch import (
    crawl_sitemap,
    fetch_llms,
    fetch_robots,
    fetch_url,
    normalize_url,
    parse_page,
)


def run_audit(
    url: str,
    max_pages: int = 20,
    sample_extra: int = 6,
    verbose: bool = True,
) -> AuditResult:
    base = normalize_url(url)
    parsed = urlparse(base)
    result = AuditResult(url=base, domain=parsed.netloc)

    def log(msg: str) -> None:
        if verbose:
            print(msg, file=sys.stderr)

    log(f"[1/6] 抓取首页… {base}")
    resp, elapsed, err = fetch_url(base)
    if err or not resp:
        result.issues.append(
            Issue(
                "critical", "可用性", f"无法访问首页：{err or '未知错误'}", base,
                "审计无法继续", "检查 DNS、SSL、防火墙", "小"
            )
        )
        compute_scores(result)
        return result

    html = resp.text
    result.homepage = parse_page(html, base)
    result.homepage["_fetch"] = {
        "url": base,
        "status": resp.status_code,
        "elapsed": elapsed,
        "size_kb": len(resp.content) / 1024,
        "security_headers": {
            "Strict-Transport-Security": resp.headers.get("Strict-Transport-Security"),
            "Content-Security-Policy": resp.headers.get("Content-Security-Policy"),
            "X-Frame-Options": resp.headers.get("X-Frame-Options"),
            "X-Content-Type-Options": resp.headers.get("X-Content-Type-Options"),
        },
    }
    result.page_samples.append({**result.homepage})

    log("[2/6] 解析 robots.txt 与 llms.txt…")
    result.robots = fetch_robots(base)
    result.llms = fetch_llms(base)

    log("[3/6] 爬取 Sitemap…")
    result.sitemap_urls = crawl_sitemap(base, max_urls=max_pages)
    result.duplicate_slugs = detect_duplicate_products(result.sitemap_urls)
    result.industry_guess, result.business_type = guess_industry(
        result.homepage, result.sitemap_urls
    )

    log(f"[4/6] 抽样分析页面（最多 {sample_extra} 个）…")
    samples = _pick_sample_urls(base, result.sitemap_urls, sample_extra)
    for i, page_url in enumerate(samples, 1):
        log(f"  [{i}/{len(samples)}] {page_url}")
        r, _, e = fetch_url(page_url, timeout=25)
        if r and r.status_code == 200:
            pdata = parse_page(r.text, page_url)
            pdata["_fetch"] = {
                "url": page_url,
                "status": r.status_code,
                "elapsed": 0,
                "size_kb": len(r.content) / 1024,
            }
            result.page_samples.append(pdata)

    result.pages_analyzed = len(result.page_samples)

    log("[5/6] 计算评分与问题清单…")
    compute_scores(result)

    log("[6/6] 完成。")
    return result


_SKIP_EXT = (
    ".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".pdf", ".zip",
    ".mp4", ".xml", ".css", ".js",
)


def _is_html_page_url(u: str) -> bool:
    low = u.lower().split("?")[0]
    if any(low.endswith(ext) for ext in _SKIP_EXT):
        return False
    if "/wp-content/uploads/" in low and not low.endswith("/"):
        return False
    return True


def _pick_sample_urls(base: str, urls: list[str], n: int) -> list[str]:
    """优先选取产品、联系、博客、shop 等模板页。"""
    html_urls = [u for u in urls if _is_html_page_url(u)]
    priority_patterns = [
        "/product/",
        "/contact",
        "/shop",
        "/about",
        "guide",
        "extrusion",
        "/jiju-",
        "/custom-aluminum",
    ]
    chosen: list[str] = []
    for pat in priority_patterns:
        for u in html_urls:
            if pat in u.lower() and u not in chosen and u.rstrip("/") != base.rstrip("/"):
                chosen.append(u)
                if len(chosen) >= n:
                    return chosen
    for u in html_urls:
        if u not in chosen and u.rstrip("/") != base.rstrip("/"):
            chosen.append(u)
        if len(chosen) >= n:
            break
    return chosen[:n]
