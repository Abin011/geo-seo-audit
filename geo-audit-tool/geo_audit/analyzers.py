# -*- coding: utf-8 -*-
"""SEO / GEO 各维度分析与问题检测（中文输出结构）。"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any
from urllib.parse import urlparse


@dataclass
class Issue:
    severity: str  # critical | high | medium | low
    category: str
    title: str
    location: str
    impact: str
    fix: str
    effort: str = "中"  # 小 | 中 | 大


@dataclass
class AuditResult:
    url: str
    domain: str
    pages_analyzed: int = 0
    issues: list[Issue] = field(default_factory=list)
    scores: dict[str, int] = field(default_factory=dict)
    projections: dict[str, str] = field(default_factory=dict)
    homepage: dict[str, Any] = field(default_factory=dict)
    robots: dict[str, Any] = field(default_factory=dict)
    llms: dict[str, Any] = field(default_factory=dict)
    sitemap_urls: list[str] = field(default_factory=list)
    page_samples: list[dict[str, Any]] = field(default_factory=list)
    duplicate_slugs: list[str] = field(default_factory=list)
    industry_guess: str = ""
    business_type: str = ""


def guess_industry(homepage: dict, sitemap_urls: list[str]) -> tuple[str, str]:
    text = " ".join(
        filter(
            None,
            [
                homepage.get("title") or "",
                homepage.get("meta_description") or "",
                " ".join(homepage.get("h1") or []),
            ],
        )
    ).lower()
    urls = " ".join(sitemap_urls[:30]).lower()
    combined = text + " " + urls

    patterns = [
        (r"aluminum|aluminium|extrusion|6063|6061|型材|铝", "铝型材挤压制造", "B2B 外贸独立站（工业制造）"),
        (r"camera|security|监控|摄像", "安防监控设备", "B2B 外贸独立站（电子安防）"),
        (r"woocommerce|product/|shop", "电商目录型", "B2B/B2C 混合（WooCommerce）"),
        (r"machinery|industrial|设备|机械", "工业设备", "B2B 外贸独立站（机械）"),
    ]
    for pat, industry, btype in patterns:
        if re.search(pat, combined):
            return industry, btype
    return "通用 B2B 外贸", "B2B 外贸独立站"


def detect_duplicate_products(urls: list[str]) -> list[str]:
    dupes = []
    for u in urls:
        path = urlparse(u).path
        if re.search(r"-\d+/?$", path) or re.search(r"-copy/?$", path):
            dupes.append(u)
    return dupes


def analyze_onpage(page: dict, label: str) -> list[Issue]:
    issues = []
    url = page.get("url", label)

    if not page.get("title"):
        issues.append(
            Issue("critical", "基础SEO", "缺少页面 Title", url,
                  "搜索引擎无法生成有效标题，CTR 极低",
                  "在 Yoast / Rank Math 中设置唯一 Title（50–60 字符）", "小")
        )
    elif page.get("title_len", 0) > 65:
        issues.append(
            Issue("medium", "基础SEO", "Title 过长可能被截断", url,
                  "搜索结果展示不完整", "压缩至 55–60 字符，前置核心关键词", "小")
        )

    if not page.get("meta_description"):
        issues.append(
            Issue("critical", "基础SEO", "缺少 Meta Description", url,
                  "Google 随机抓取摘要，CTR 不可控",
                  "Yoast 产品页模板：%%title%% + 合金 + MOQ + ISO + CTA", "小")
        )
    elif page.get("meta_desc_len", 0) < 70:
        issues.append(
            Issue("medium", "基础SEO", "Meta Description 过短", url,
                  "摘要信息不足，难以吸引点击",
                  "扩展至 120–155 字符，含卖点与行动号召", "小")
        )

    h1s = page.get("h1") or []
    if len(h1s) == 0:
        issues.append(
            Issue("high", "基础SEO", "页面缺少 H1", url,
                  "主题信号弱，AI 难以判断页面主旨",
                  "添加唯一 H1，包含主关键词", "小")
        )
    elif len(h1s) > 1:
        issues.append(
            Issue("critical", "基础SEO", f"存在 {len(h1s)} 个 H1（应仅 1 个）", url,
                  "分散排名权重，违反 SEO 最佳实践",
                  "将全局横幅标题降为 H2 或 div，保留产品名称为唯一 H1", "小")
        )

    if not page.get("canonical"):
        issues.append(
            Issue("high", "基础SEO", "缺少 Canonical 标签", url,
                  "可能导致重复 URL 被分别索引",
                  "Yoast 开启 canonical；检查 shop 归档页", "小")
        )

    if page.get("img_total", 0) > 0 and page.get("img_no_alt", 0) > 0:
        issues.append(
            Issue("medium", "基础SEO", f"{page['img_no_alt']} 张图片缺少 alt 属性", url,
                  "图片搜索与无障碍均受损",
                  "批量补全描述性 alt 文本", "中")
        )

    return issues


def analyze_schema(pages: list[dict]) -> tuple[list[Issue], int]:
    issues = []
    all_types: set[str] = set()
    product_pages = [p for p in pages if "/product/" in p.get("url", "")]
    has_product_schema = False

    for p in pages:
        types = set(p.get("schema_types") or [])
        all_types |= types
        if "Product" in types:
            has_product_schema = True

    score = 40
    if "Organization" in all_types:
        score += 10
    if "WebSite" in all_types:
        score += 5
    if "BreadcrumbList" in all_types:
        score += 5
    if "Article" in all_types:
        score += 5
    if has_product_schema:
        score += 20
    else:
        if product_pages:
            issues.append(
                Issue(
                    "critical", "结构化数据",
                    f"共 {len(product_pages)} 个产品页未检测到 Product Schema",
                    "全站产品 URL",
                    "Google 富媒体结果与 AI 无法提取规格、报价、SKU",
                    "部署 Product + Offer JSON-LD（见 schema/d_product_template.json）",
                    "中",
                )
            )
    for missing, name in [
        ("FAQPage", "FAQPage"),
        ("HowTo", "HowTo"),
        ("LocalBusiness", "LocalBusiness / Manufacturer"),
    ]:
        if missing not in all_types:
            issues.append(
                Issue(
                    "high", "结构化数据", f"全站缺少 {name} Schema", "全站",
                    "AI 问答与本地/制造实体识别受限",
                    f"在首页/FAQ/关于页注入 {missing} JSON-LD",
                    "中",
                )
            )
            score -= 5

    return issues, min(100, max(0, score))


def analyze_technical(
    homepage_fetch: dict,
    robots: dict,
    llms: dict,
    pages_timing: list[dict],
) -> tuple[list[Issue], int]:
    issues = []
    score = 70

    ttfb = homepage_fetch.get("elapsed", 0)
    size_kb = homepage_fetch.get("size_kb", 0)
    if ttfb > 1.5:
        issues.append(
            Issue(
                "critical", "技术SEO",
                f"首页 TTFB 过慢（{ttfb:.2f}s，建议 <1.5s）",
                homepage_fetch.get("url", ""),
                "Core Web Vitals 与 Google AI Overview 抓取效率受损",
                "开启 Hostinger HCDN 页面缓存；WP-Rocket 预加载站点地图",
                "小",
            )
        )
        score -= 15
    if size_kb > 400:
        issues.append(
            Issue(
                "high", "技术SEO",
                f"首页 HTML 体积过大（{size_kb:.0f} KB）",
                homepage_fetch.get("url", ""),
                "LCP 与 INP 恶化",
                "延迟加载 JS、合并 CSS、禁用无用 Elementor 组件",
                "中",
            )
        )
        score -= 10

    sec = homepage_fetch.get("security_headers") or {}
    for h in ["Strict-Transport-Security", "Content-Security-Policy", "X-Frame-Options"]:
        if not sec.get(h):
            issues.append(
                Issue(
                    "high", "技术SEO", f"缺少安全响应头：{h}", "全站 HTTP 响应",
                    "信任信号与安全评分偏低",
                    "在 .htaccess 或 CDN 面板添加标准安全头",
                    "小",
                )
            )
            score -= 3

    if robots.get("duplicate_user_agent"):
        issues.append(
            Issue(
                "critical", "GEO 技术",
                "robots.txt 存在重复 User-agent 块",
                robots.get("url", "/robots.txt"),
                "爬虫解析歧义，AI 爬虫无明确 Allow",
                "替换为带显式 AI 爬虫 Allow 的标准 robots.txt",
                "小",
            )
        )
        score -= 8

    implicit = sum(
        1 for v in (robots.get("ai_crawler_status") or {}).values()
        if v == "implicit_allow"
    )
    if implicit > 10:
        issues.append(
            Issue(
                "medium", "GEO 技术",
                f"{implicit} 个 AI 爬虫仅隐式允许（未显式 Allow）",
                "/robots.txt",
                "部分 AI 引擎保守不抓取",
                "为 GPTBot、ClaudeBot、PerplexityBot 等添加显式 Allow",
                "小",
            )
        )

    if not llms.get("exists"):
        issues.append(
            Issue(
                "high", "GEO 技术", "未部署 llms.txt",
                "/llms.txt",
                "ChatGPT / Perplexity 等无法快速理解站点结构",
                "发布手工 curated 的 llms.txt（含核心页面摘要）",
                "中",
            )
        )
        score -= 12
    elif llms.get("has_chinese") and llms.get("size", 0) > 10000:
        issues.append(
            Issue(
                "medium", "GEO 技术",
                "llms.txt 含中文或 HTML 实体，描述截断",
                "/llms.txt",
                "英文 B2B 站点 AI 引用质量下降",
                "用英文重写 llms.txt，去除 &hellip; 与重复 boilerplate",
                "中",
            )
        )
        score -= 5

    return issues, min(100, max(0, score))


def analyze_content_geo(pages: list[dict], homepage: dict) -> tuple[list[Issue], int]:
    issues = []
    score = 55

    wc = homepage.get("word_count", 0)
    if wc < 800:
        issues.append(
            Issue(
                "medium", "内容SEO",
                f"首页正文过薄（约 {wc} 词）",
                homepage.get("url", "/"),
                "难以覆盖主题集群与 EEAT",
                "增加工厂数据表、行业应用模块、FAQ 区块",
                "中",
            )
        )
        score -= 8

    if not homepage.get("has_faq_keyword"):
        issues.append(
            Issue(
                "high", "GEO 内容",
                "首页无 FAQ / 问答结构",
                "/",
                "AI Overview / Perplexity 难以引用问答片段",
                "添加 6+ 条 B2B 采购 FAQ 并部署 FAQPage Schema",
                "中",
            )
        )
        score -= 10

    if homepage.get("js_external", 0) > 30:
        issues.append(
            Issue(
                "high", "技术SEO",
                f"首页加载 {homepage['js_external']} 个外部 JS",
                "/",
                "INP 与可抓取性变差",
                "WP-Rocket 延迟 JS + 删除未使用脚本",
                "中",
            )
        )
        score -= 8

    product_thin = [
        p for p in pages
        if "/product/" in p.get("url", "")
        and p.get("word_count", 0) < 200
        and not p.get("meta_description")
    ]
    if len(product_thin) > 5:
        issues.append(
            Issue(
                "critical", "内容SEO",
                f"约 {len(product_thin)} 个产品页内容过薄且无 Meta",
                "产品 URL",
                "大量产品页无法参与排名与 AI 引用",
                "替换重复 Product Parameters 模板为合金专属技术说明",
                "大",
            )
        )
        score -= 15

    if not any("hreflang" in str(p.get("hreflang")) for p in pages):
        issues.append(
            Issue(
                "high", "国际SEO",
                "全站未配置 hreflang",
                "<head>",
                "多语言/多市场 B2B 站点无法正确地理定位",
                "添加 x-default + en（后续 de/es）",
                "小",
            )
        )
        score -= 10

    return issues, min(100, max(0, score))


def score_citability(homepage: dict) -> int:
    """简易 AI 可引用性评分。"""
    text = " ".join(
        filter(
            None,
            [
                homepage.get("meta_description") or "",
                " ".join(homepage.get("h1") or []),
            ],
        )
    )
    score = 30
    if re.search(r"\d{4}", text):
        score += 10
    if re.search(r"\d+[,]?\d*\s*(t|ton|tonne|吨|press|ISO)", text, re.I):
        score += 15
    if re.search(r"ISO\s*\d{4,5}", text):
        score += 10
    if homepage.get("word_count", 0) > 1000:
        score += 15
    if homepage.get("has_faq_keyword"):
        score += 10
    return min(100, score)


def compute_scores(result: AuditResult) -> None:
    tech_issues, tech = analyze_technical(
        result.homepage.get("_fetch") or {},
        result.robots,
        result.llms,
        [],
    )
    schema_issues, schema = analyze_schema(result.page_samples)
    content_issues, content = analyze_content_geo(
        result.page_samples, result.homepage
    )
    citability = score_citability(result.homepage)

    all_onpage: list[Issue] = []
    for p in result.page_samples[:8]:
        all_onpage.extend(analyze_onpage(p, p.get("url", "")))

    result.issues = tech_issues + schema_issues + content_issues + all_onpage

    if result.duplicate_slugs:
        result.issues.insert(
            0,
            Issue(
                "critical", "技术SEO",
                f"发现 {len(result.duplicate_slugs)} 个疑似重复产品 URL（-2/-copy 等后缀）",
                "产品目录",
                "分散链接权重，触发重复内容警告",
                "选定主 URL → 301 重定向 → 删除重复 WooCommerce 产品",
                "中",
            ),
        )
        tech = max(0, tech - 10)

    brand = 25
    platform = 28
    if result.llms.get("exists"):
        platform += 8
    if any(t == "Product" for p in result.page_samples for t in (p.get("schema_types") or [])):
        platform += 10

    geo = int(
        citability * 0.25
        + brand * 0.20
        + content * 0.20
        + tech * 0.15
        + schema * 0.10
        + platform * 0.10
    )
    seo = int(tech * 0.25 + content * 0.20 + content * 0.20 + schema * 0.10 + 35)

    result.scores = {
        "SEO总分": min(100, seo),
        "GEO总分": min(100, geo),
        "技术SEO": tech,
        "内容质量": content,
        "结构化数据": schema,
        "AI可引用性": citability,
        "品牌权威": brand,
        "平台优化": platform,
    }
    result.projections = {
        "自然流量增长": "+60% ~ +90%（90天全量执行）",
        "AI曝光增长": "+250% ~ +400%",
        "询盘增长": "+35% ~ +65%",
        "GEO目标分": "78/100",
        "SEO目标分": "80/100",
    }


def rating_label(score: int) -> str:
    if score >= 90:
        return "优秀"
    if score >= 75:
        return "良好"
    if score >= 60:
        return "中等"
    if score >= 40:
        return "较差"
    return "危急"
