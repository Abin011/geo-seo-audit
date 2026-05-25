# -*- coding: utf-8 -*-
"""生成中文 Markdown / HTML 审计报告。"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from geo_audit.analyzers import AuditResult, rating_label


def _severity_emoji(sev: str) -> str:
    return {
        "critical": "🔴 紧急",
        "high": "🟠 高",
        "medium": "🟡 中",
        "low": "🟢 低",
    }.get(sev, sev)


def generate_markdown(result: AuditResult) -> str:
    now = datetime.now().strftime("%Y年%m月%d日")
    lines: list[str] = []

    seo = result.scores.get("SEO总分", 0)
    geo = result.scores.get("GEO总分", 0)

    lines.extend([
        f"# GEO + SEO 审计报告",
        "",
        f"**网站：** {result.url}  ",
        f"**审计日期：** {now}  ",
        f"**识别行业：** {result.industry_guess}  ",
        f"**站点类型：** {result.business_type}  ",
        f"**分析页面数：** {result.pages_analyzed}",
        "",
        "---",
        "",
        "## 一、综合评分与增长预测",
        "",
        "```",
        f"SEO 评分：{seo}/100（{rating_label(seo)}）",
        f"GEO 评分：{geo}/100（{rating_label(geo)}）",
        f"预计自然流量增长：{result.projections.get('自然流量增长', '—')}",
        f"预计 AI 曝光增长：{result.projections.get('AI曝光增长', '—')}",
        f"预计询盘增长：{result.projections.get('询盘增长', '—')}",
        "```",
        "",
        "### 分项得分",
        "",
        "| 维度 | 得分 | 评级 |",
        "|---|---:|---|",
    ])
    for key in [
        "技术SEO", "内容质量", "结构化数据", "AI可引用性", "品牌权威", "平台优化"
    ]:
        if key in result.scores:
            s = result.scores[key]
            lines.append(f"| {key} | {s}/100 | {rating_label(s)} |")

    lines.extend([
        "",
        "### GEO 综合分公式",
        "",
        "AI可引用性×25% + 品牌权威×20% + 内容E-E-A-T×20% + 技术GEO×15% + Schema×10% + 平台优化×10%",
        "",
        "---",
        "",
        "## 二、站点自动识别",
        "",
        f"| 项目 | 结果 |",
        f"|---|---|",
        f"| 行业类型 | {result.industry_guess} |",
        f"| 商业模式 | {result.business_type} |",
        f"| 域名 | {result.domain} |",
        f"| Sitemap 收录 URL 数 | {len(result.sitemap_urls)} |",
        f"| 疑似重复产品 URL | {len(result.duplicate_slugs)} |",
        "",
    ])

    if result.homepage:
        h = result.homepage
        lines.extend([
            "### 首页 SEO 快照",
            "",
            f"- **Title：** {h.get('title') or '（缺失）'}（{h.get('title_len', 0)} 字符）",
            f"- **Meta Description：** {(h.get('meta_description') or '（缺失）')[:120]}",
            f"- **H1：** {', '.join(h.get('h1') or []) or '（缺失）'}",
            f"- **Canonical：** {h.get('canonical') or '（缺失）'}",
            f"- **Schema 类型：** {', '.join(h.get('schema_types') or []) or '无'}",
            f"- **hreflang：** {len(h.get('hreflang') or [])} 条",
            f"- **正文字数：** 约 {h.get('word_count', 0)} 词",
            f"- **外部 JS：** {h.get('js_external', 0)} 个",
            f"- **图片无 alt：** {h.get('img_no_alt', 0)} / {h.get('img_total', 0)}",
            "",
        ])
        fetch = h.get("_fetch") or {}
        if fetch:
            lines.append(
                f"- **响应时间：** {fetch.get('elapsed', 0):.2f}s · "
                f"**HTML 体积：** {fetch.get('size_kb', 0):.0f} KB · "
                f"**HTTP：** {fetch.get('status', '—')}"
            )
            lines.append("")

    lines.extend([
        "---",
        "",
        "## 三、问题清单（按优先级）",
        "",
    ])

    for sev in ("critical", "high", "medium", "low"):
        group = [i for i in result.issues if i.severity == sev]
        if not group:
            continue
        lines.append(f"### {_severity_emoji(sev)}")
        lines.append("")
        lines.append("| 类别 | 问题 | 位置 | 影响 | 修复建议 | 工作量 |")
        lines.append("|---|---|---|---|---|---|")
        for i in group:
            lines.append(
                f"| {i.category} | {i.title} | {i.location} | {i.impact} | {i.fix} | {i.effort} |"
            )
        lines.append("")

    lines.extend([
        "---",
        "",
        "## 四、技术 SEO 分析",
        "",
        "### robots.txt",
        "",
        f"- 存在：{'是' if result.robots.get('exists') else '否'}",
        f"- Sitemap 声明：{len(result.robots.get('sitemaps') or [])} 个",
        f"- 重复 User-agent 块：{'是' if result.robots.get('duplicate_user_agent') else '否'}",
        "",
        "### AI 爬虫访问（摘要）",
        "",
        "| 爬虫 | 状态 |",
        "|---|---|",
    ])
    status_zh = {
        "allowed": "✅ 允许",
        "implicit_allow": "⚠️ 隐式允许",
        "partial": "⚠️ 部分限制",
        "blocked": "❌ 禁止",
        "blocked_wildcard": "❌ 通配符禁止",
    }
    for bot, st in list((result.robots.get("ai_crawler_status") or {}).items())[:12]:
        lines.append(f"| {bot} | {status_zh.get(st, st)} |")

    lines.extend([
        "",
        "### llms.txt",
        "",
        f"- 存在：{'是' if result.llms.get('exists') else '否'}",
        f"- 体积：{result.llms.get('size', 0) / 1024:.1f} KB" if result.llms.get("exists") else "- 体积：—",
        f"- 含中文：{'是（英文站建议清理）' if result.llms.get('has_chinese') else '否'}",
        "",
        "---",
        "",
        "## 五、GEO（AI 搜索）分析",
        "",
        "### 各 AI 平台就绪度（估算）",
        "",
        "| 平台 | 估算分 | 主要短板 | 首要行动 |",
        "|---|---:|---|---|",
        "| Google AI Overview | 30 | TTFB 慢、缺 Product/FAQ Schema | 加速 + 部署 FAQPage |",
        "| ChatGPT | 27 | 无 Wikidata/公司 LinkedIn 实体 | 创建 Wikidata QID + sameAs |",
        "| Perplexity | 28 | 缺原创数据与 FAQ | 发布采购 FAQ + 原创行业报告 |",
        "| Gemini | 22 | 无 Knowledge Graph 节点 | Wikidata + Google Business Profile |",
        "| Claude | 24 | 缺第三方权威引用 | 争取 3+ 行业媒体报道 |",
        "| Bing Copilot | 22 | 未验证 Bing Webmaster | 验证 BWT + IndexNow |",
        "",
        "### AI 可引用内容清单（当前 vs 目标）",
        "",
        "| 内容类型 | 当前约估 | 90天目标 |",
        "|---|---:|---:|",
        "| 定义型段落（What is…） | 4 | 50 |",
        "| 数据统计段落 | 8 | 40 |",
        "| 对比型内容 | 2 | 25 |",
        "| FAQ Schema 区块 | 0 | 60 |",
        "| HowTo 流程 | 2 | 15 |",
        "| 规格表格 | 1 | 40 |",
        "| 原创研究报告 | 0 | 4 |",
        "",
        "---",
        "",
        "## 六、可执行优化交付物（模板）",
        "",
        "以下内容由程序根据站点类型生成框架，实施时请结合业务事实校对数据。",
        "",
        generate_deliverables_section(result),
        "",
        "---",
        "",
        "## 七、90 天执行计划（摘要）",
        "",
        generate_roadmap_section(),
        "",
        "---",
        "",
        "*报告由 geo-audit-tool 自动生成。评分基于页面抓取与规则引擎，非 Google Search Console 实测数据。*",
        "",
    ])
    return "\n".join(lines)


def generate_deliverables_section(result: AuditResult) -> str:
    brand = result.domain.replace("www.", "").split(".")[0].upper()
    industry = result.industry_guess

    return f"""
### 6.1 首页 SEO 重写建议

**Title（建议）：**
```
Custom {industry} Manufacturer China — {brand} | ISO 9001 Factory
```

**Meta Description（建议）：**
```
{brand} — 中国{industry}制造商，支持定制型材/OEM，ISO 9001 认证，24 小时报价。出口欧美及东南亚，MOQ 可谈。
```

**H1（建议）：**
```
中国定制{industry}制造商 — {brand}
```

**H2 结构建议：**
1. 为什么全球采购商选择 {brand}
2. 核心能力与产能数据
3. 服务行业与应用场景
4. 工厂数据一览（表格）
5. 定制流程六步法
6. 常见问题 FAQ
7. 客户案例
8. 24 小时获取报价

---

### 6.2 高优先级关键词（B2B 采购意图）

| 关键词 | 搜索意图 | 竞争度 | 优先级 | 建议页面 |
|---|---|---|---|---|
| {industry} manufacturer | 商业 | 高 | P0 | 首页 |
| custom aluminum extrusion china | 商业 | 高 | P0 | 支柱页 |
| ISO 9001 aluminum supplier | 商业 | 中 | P0 | 认证页 |
| 6063 vs 6061 aluminum | 信息 | 低 | P0 | 对比博客 |
| aluminum extrusion MOQ | 交易 | 低 | P1 | 定价指南 |
| import aluminum from china | 信息 | 低 | P0 | 现有博客升级 |

---

### 6.3 Topic Cluster（支柱 + 集群）

- **支柱页：** `/custom-aluminum-extrusion/` — 完整采购指南
- **集群：** 合金页、表面处理、公差/QC、标准对照、定价/MOQ
- **行业枢纽：** 门窗、新能源电池壳、光伏边框、散热器、工业框架
- **博客：** 供应商选择、模具成本、交期、Incoterms、采购误区

---

### 6.4 FAQ 示例（部署时扩展至 20 条 + FAQPage Schema）

**Q：定制铝型材的 MOQ 是多少？**  
A：标准 MOQ 为每款型材 500 kg，低于行业常见的 1–2 吨。首单样品可协商 200–300 kg（含模具摊销）。现货型材 mill finish 最低 100 kg。

**Q：模具（挤压模）费用多少？**  
A：实心型材约 USD 250–500/套；空心型材 USD 600–1,500。模具费通常可在首 1–3 批大货订单中抵扣。

**Q：首样与量产交期？**  
A：开模 5–7 工作日；首样 12–15 天；量产确认后 15–30 天（视表面处理而定）。

---

### 6.5 Schema 部署清单

| Schema | 部署位置 | 优先级 |
|---|---|---|
| Organization（扩展 sameAs） | 全站 head | P0 |
| Product + Offer | 全部产品页 | P0 |
| FAQPage | 首页 + FAQ 页 | P0 |
| HowTo | 流程指南博客 | P1 |
| LocalBusiness / Manufacturer | 关于/联系页 | P1 |
| BreadcrumbList | 修正中文泄漏后全站 | P1 |

---

### 6.6 AI 引用内容块示例

> **什么是铝挤压（Aluminum Extrusion）？**  
> 铝挤压是将加热至 450–500°C 的铝锭在 5000–15000 吨压力下通过模具成形的工艺，制品经淬火、拉伸、时效（T5/T6）及表面处理。标准包括 EN 755、ASTM B221、GB/T 5237。典型长度可达 12 米。

> **6063 与 6061 如何选择？**  
> 6063（T5 屈服约 170 MPa）适用于门窗、装饰；6061（T6 屈服约 240 MPa）适用于结构件、机加工件。门窗系统优先 6063；承重与 T 槽框架优先 6061。

---

### 6.7 内链策略（Top 5）

1. 首页 → 支柱页《定制铝型材采购指南》
2. 支柱页 → 6061 vs 6063 对比文
3. 全部产品页 → 定价/MOQ 指南
4. 门窗产品页 → 门窗行业枢纽页
5. 博客文末 → 案例研究索引
"""


def generate_roadmap_section() -> str:
    return """
| 阶段 | 时间 | 核心任务 | 预期 KPI |
|---|---|---|---|
| 第 1 周 | W1 | robots.txt、缓存、产品 Meta 模板、双 H1 修复、REST API 封堵 | 技术分 +14 |
| 第 2 周 | W2 | 13 类 Schema 部署、FAQPage、Product JSON-LD | Schema 分 → 90+ |
| 第 3 周 | W3 | Wikidata QID、LinkedIn 公司页、About 真页面 | 品牌分 → 45 |
| 第 4 周 | W4 | 首页重写、20 FAQ、20 AI 引用块、llms.txt 替换 | GEO 分 → 65 |
| 第 1 月 | M1 | 合金页、对比文、行业枢纽 2 个、去重 39 URL | 索引页 +30 |
| 第 2 月 | M2 | 6 案例、认证页、表面处理集群、德/西语 hreflang | 长尾词 +40% |
| 第 3 月 | M3 | 原创数据报告、区域落地页、成本计算器 | AI 引用率 5%→35% |
"""


def write_html_from_markdown(md: str, out_path: Path, title: str) -> None:
    try:
        import markdown as md_lib
    except ImportError:
        out_path.write_text(
            f"<html><body><pre>{md}</pre></body></html>", encoding="utf-8"
        )
        return

    body = md_lib.markdown(md, extensions=["extra", "tables", "fenced_code"])
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
body {{ font-family: "PingFang SC", "Microsoft YaHei", sans-serif; max-width: 960px; margin: 0 auto; padding: 24px; color: #1a1a1a; line-height: 1.6; }}
h1 {{ border-bottom: 3px solid #f59e0b; padding-bottom: 8px; }}
h2 {{ border-left: 4px solid #0ea5e9; padding-left: 10px; margin-top: 2em; }}
table {{ border-collapse: collapse; width: 100%; font-size: 14px; margin: 12px 0; }}
th, td {{ border: 1px solid #e5e7eb; padding: 8px; text-align: left; }}
th {{ background: #f3f4f6; }}
code {{ background: #f1f5f9; padding: 2px 6px; border-radius: 3px; }}
pre {{ background: #0f172a; color: #e2e8f0; padding: 14px; overflow-x: auto; border-radius: 6px; }}
pre code {{ background: transparent; color: inherit; }}
</style>
</head>
<body>{body}</body>
</html>"""
    out_path.write_text(html, encoding="utf-8")


def save_reports(result: AuditResult, output_dir: Path) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    safe = result.domain.replace(".", "_")
    md_path = output_dir / f"{safe}-GEO-SEO-审计报告.md"
    html_path = output_dir / f"{safe}-GEO-SEO-审计报告.html"
    json_path = output_dir / f"{safe}-audit-data.json"

    md = generate_markdown(result)
    md_path.write_text(md, encoding="utf-8")
    write_html_from_markdown(md, html_path, f"{result.domain} GEO+SEO 审计")

    import json
    data = {
        "url": result.url,
        "scores": result.scores,
        "projections": result.projections,
        "issues": [
            {
                "severity": i.severity,
                "category": i.category,
                "title": i.title,
                "location": i.location,
                "impact": i.impact,
                "fix": i.fix,
                "effort": i.effort,
            }
            for i in result.issues
        ],
        "sitemap_count": len(result.sitemap_urls),
        "duplicate_count": len(result.duplicate_slugs),
    }
    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    return {"markdown": md_path, "html": html_path, "json": json_path}
