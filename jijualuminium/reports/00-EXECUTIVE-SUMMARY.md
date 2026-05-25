# JIJU Aluminium — GEO + SEO Master Audit Report

**Audit Date:** 25 May 2026
**Site Audited:** https://jijualuminium.com/
**Company:** Shandong JIJU Aluminium Industry Co., Ltd.
**Industry:** B2B Custom Aluminum Extrusion Manufacturing (foreign-trade independent site)
**Tech Stack:** WordPress + WooCommerce + Yoast SEO + Hostinger + HCDN
**Pages Crawled:** 7 pages, 137 product URLs, 56 product categories, 53 blog posts

---

## SCORES & PROJECTIONS

```
SEO Score:    42 / 100  (Poor — Fair foundation, weak execution)
GEO Score:    37 / 100  (Poor — invisible to AI engines today)

Projected 90-day uplift (full execution of this plan):
  • Google organic traffic         :  +60% to +90%
  • AI search exposure / citations :  +250% to +400%
  • Inquiry / quote-request volume :  +35% to +65%
  • Composite GEO Score            :  37 → 78 / 100
  • Composite SEO Score            :  42 → 80 / 100
```

### Score Breakdown (GEO Composite, weighted)

| Category | Weight | Current | Target (90d) | Source |
|---|---|---|---|---|
| AI Citability | 25% | 35 / 100 | 80 | content + platform audits |
| Brand Authority | 20% | 25 / 100 | 65 | manual scan |
| Content E-E-A-T | 20% | 30 / 100 | 75 | content audit |
| Technical GEO | 15% | 58 / 100 | 85 | technical audit |
| Schema & Structured Data | 10% | 58 / 100 | 92 | schema audit |
| Platform Optimization | 10% | 26 / 100 | 75 | platform audit |
| **Composite GEO** | 100% | **37 / 100** | **78 / 100** | |

### Score Breakdown (SEO Composite, weighted)

| Category | Weight | Current | Target (90d) |
|---|---|---|---|
| Technical SEO | 25% | 58 / 100 | 85 |
| On-page (titles, meta, H1, content) | 20% | 40 / 100 | 80 |
| Content depth & topical authority | 20% | 37 / 100 | 78 |
| Internal links / site architecture | 10% | 35 / 100 | 75 |
| International SEO (hreflang, geo) | 10% | 15 / 100 | 70 |
| Structured data | 10% | 58 / 100 | 92 |
| Off-page authority | 5% | 20 / 100 | 50 |
| **Composite SEO** | 100% | **42 / 100** | **80 / 100** |

---

## EXECUTIVE NARRATIVE

JIJU has the **raw material of a tier-1 B2B aluminum extrusion site** — a real 30-year-old factory with verifiable scale (150,000 t/year, 21 presses, 300,000 m², ISO 9001/14001/45001), a cornerstone blog post with genuine engineering depth, a 137-product catalog already crawled by Google, and a permissive `robots.txt` that lets every AI bot in. The site is server-rendered, on HTTP/2 + Brotli, and Yoast already emits valid baseline schema on every page.

Yet today, **JIJU is largely invisible to AI search engines** and underperforming on Google for high-intent B2B queries. Six concrete failure modes explain it:

1. **Edge cache misses everywhere** — every URL returns `x-hcdn-cache-status: BYPASS`. WP-Rocket is installed but Hostinger HCDN is not warming. TTFB is 1.3–1.8 s and total load 5–6 s — far below Google's SGE / Perplexity TTFB thresholds.
2. **Commerce-critical schema is missing** — zero Product schema across 137 WooCommerce pages, zero FAQPage, zero HowTo, zero LocalBusiness/Manufacturer. Yoast emits the basic graph but stops there. AI engines have no structured way to extract specs, prices, MOQs, or lead times.
3. **No AI entity** — "Shandong JIJU Aluminium" has no Wikidata QID, no Wikipedia stub, no company LinkedIn page (only a personal `/in/` profile), and a non-branded YouTube channel (`@JackieWang-g7q`). ChatGPT, Gemini, and Claude have no canonical entity to reference.
4. **Content quality undermines authority** — most product pages share **identical boilerplate** ("Product Parameters Standard: European standard, national standard..."), product pages have **two H1s** with a typo ("ALUMINUMEXTRUSION"), 39 of 137 product slugs are duplicates (`-2`, `-3`, ..., `-copy`), the about page renders as a blog index, blog posts are written in obvious AI first-person voice ("I trust JIJU..."), and key factory stats conflict between sections (150,000 t vs 50,000 t vs 24,000 m² vs "0 employees" displayed).
5. **No international SEO** despite global B2B targeting — no `hreflang`, no regional landing pages, no localized currencies/Incoterms guidance.
6. **The `llms.txt` exists** (37 KB, 174 lines) but has placeholder title/description and contains Chinese characters, HTML entities, and truncated descriptions — net helpful but not maximizing AI ingestion quality.

**The good news:** every issue is fixable, and most can be fixed with WordPress filters, Yoast templates, schema injections, and structured-content publishing — no migration needed. **Realistic 90-day uplift assuming full execution of the action plan in this report**: composite GEO score 37 → 78, AI citation rate +250–400%, organic traffic +60–90%, and inquiry volume +35–65%.

---

## REPORT INDEX

| File | Contents |
|---|---|
| `00-EXECUTIVE-SUMMARY.md` (this file) | Scores, projections, narrative |
| `01-CRITICAL-ISSUES.md` | All Critical/High/Medium/Low issues with fixes |
| `02-PAGE-LEVEL-ANALYSIS.md` | Per-template analysis: home, category, product, blog, about, contact, shop |
| `03-COMPETITOR-BENCHMARK.md` | Top 5 competitors + tactics to copy |
| `04-REWRITTEN-HOMEPAGE.md` | New Title, Meta, H1, H2 structure for homepage |
| `05-KEYWORD-STRATEGY.md` | Top 30 keywords + Topic Cluster map |
| `06-FAQ-LIBRARY.md` | 20 ready-to-publish B2B FAQs (with FAQPage schema) |
| `07-AI-CITATION-BLOCKS.md` | 20 AI-quotable content blocks (What is / How / Why / Benefits / Applications / Difference) |
| `08-SCHEMA-DEPLOYMENT.md` | All 13 JSON-LD schemas + WordPress deployment guide |
| `09-INTERNAL-LINKING-MAP.md` | Internal-linking strategy + top 30 link actions |
| `10-90-DAY-ACTION-PLAN.md` | Week 1, Week 2, Month 1, Month 2, Month 3 plan |
| `11-ROBOTS-AND-LLMSTXT.md` | Drop-in `robots.txt` and improved `llms.txt` |
| `JIJU-GEO-SEO-CLIENT-REPORT.pdf` | Presentation-ready client deliverable |

Source-of-truth subagent reports remain at:
- `/tmp/jiju_technical_report.md` (technical, 615 lines)
- `/tmp/jiju_content_report.md` (content/EEAT)
- `/tmp/jiju_schema_report.md` + `/tmp/jiju_schema/` (schema + 13 JSON-LD files)
- `/tmp/jiju_platform_report.md` (platform analysis, 516 lines)

---
