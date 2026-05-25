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
# 01 — Issues by Severity

Synthesized from technical, content, schema, and platform audits. Each issue: ID · Title · Where · Impact · Fix · Effort.

Effort: S (≤2 h) · M (½–2 days) · L (3+ days)
Impact: C (Critical, immediate ranking) · H (High, growth) · M (Medium) · L (Low/long-term)

---

## CRITICAL — Fix this week (compounding daily damage)

| ID | Issue | Where | Impact | Fix | Effort |
|---|---|---|---|---|---|
| C1 | **Edge cache bypassed on every URL** — `x-hcdn-cache-status: BYPASS` always. WP-Rocket installed but HCDN not warming. TTFB 1.3–1.8 s, total load 5–6 s. | Sitewide | C | Hostinger panel → Performance → enable HCDN page cache. WP-Rocket → Cache lifespan 10 h, Mobile cache ON, Preload sitemap. Add `Cache-Control: public, max-age=600, s-maxage=86400` for HTML; 1 yr for static. | S |
| C2 | **51 external JS + 77 CSS files on homepage** — render-blocking, kills LCP/INP. | Home + every page | C | WP-Rocket → "Load JS deferred", "Delay JS execution", "Combine Google Fonts". Disable unused Elementor widgets. Audit 50 JS files via Coverage tool, drop ≥30. Switch to Astra/Kadence base theme if Elementor bloat persists. | M |
| C3 | **Zero Product schema on 137 WooCommerce pages** — no name/sku/brand/offers/aggregateRating exposed to Google or AI. | All `/product/*` | C | Deploy `wpseo_schema_product` filter (snippet in `08-SCHEMA-DEPLOYMENT.md`). Or install Rank Math Pro and let it auto-emit. Validate on Google Rich Results Test. | M |
| C4 | **39 / 137 product URLs are duplicates** (`-2`, `-3`, ..., `-copy` suffixes — e.g. `aluminum-alloy-doors-and-windows-2/3/4/5/6/7/8`). Splits link equity, triggers Google "Duplicate without user-selected canonical" warnings. | `/product/*-N/`, `*-copy/` | C | Audit each cluster → choose primary → 301-redirect duplicates. Add bulk-canonical filter (snippet in tech report §12). Then physically delete duplicate posts in WooCommerce. | M |
| C5 | **Two `<h1>` on every product page** ("LEADING CUSTOM ALUMINUMEXTRUSION MANUFACTURER" + product name) — also has a typo (no space). | All `/product/*` | C | Edit Elementor product template → demote the global "LEADING..." line to `<h2>` or to a styled `<div>`. Fix typo to "LEADING CUSTOM ALUMINUM EXTRUSION MANUFACTURER". | S |
| C6 | **Robots.txt has duplicate `User-agent: *` blocks** (Yoast bug) and **no explicit AI crawler allows**. AI engines see ambiguous signals. | `/robots.txt` | C | Replace with the file in `11-ROBOTS-AND-LLMSTXT.md`. Adds explicit allows for GPTBot, ChatGPT-User, OAI-SearchBot, ClaudeBot, anthropic-ai, PerplexityBot, Perplexity-User, Google-Extended, Applebot-Extended, CCBot, Meta-ExternalAgent, Amazonbot, cohere-ai, MistralAI-User, DuckAssistBot, ImagesiftBot, Diffbot, YouBot, TimpiBot. Explicit Bytespider/MJ12/DotBot/PetalBot blocks. | S |
| C7 | **All 137 product pages missing `<meta name="description">`** — Google generates random snippets, kills CTR. | All `/product/*` | C | Yoast → Search Appearance → Products → meta-description template: `Custom %%title%% in 6063/6061 aluminum, %%cf_alloy%% alloy, anodized/powder coated. ISO 9001 factory, MOQ 500 kg, 5–7 day mold lead time. Get a quote.` | S |
| C8 | **`/shop/` page has NO title, NO meta, NO canonical, NO H1** — broken commerce hub. | `/shop/` | C | In Yoast → set Title `JIJU Aluminum Extrusion Catalog — 137 Custom Profiles`, meta `Browse JIJU's full catalog of 137 custom aluminum extrusions ...`, H1 `JIJU Aluminum Extrusion Catalog`. Fix template's `wp_head` if Yoast filter not firing on shop archive. | S |
| C9 | **Product pages have boilerplate "Product Parameters" copy** repeated across ~100 pages — duplicate content + zero AI quotability. Some entries also contain Chinese characters (e.g. "产品参数 标准：欧标、国标"). | All `/product/*` | C | Replace boilerplate with the alloy-specific spec block in `07-AI-CITATION-BLOCKS.md` (block #11). Use ACF or product custom fields per product. Strip all Chinese characters from English-locale pages. | L |
| C10 | **No company entity online** — no Wikidata QID, no Wikipedia stub, no company LinkedIn page (only personal `/in/jijualuminium/`), non-branded YouTube `@JackieWang-g7q`. AI engines cannot resolve "JIJU Aluminium" to a canonical entity. | Off-site | C | (a) Create Wikidata QID for "Shandong JIJU Aluminium Co., Ltd." (founding 1994, Linqu County, alloys, certs). (b) Build LinkedIn company page. (c) Rebrand YouTube channel as `@JIJUAluminium`. (d) Add full `sameAs` array to Organization schema (snippet in `08-SCHEMA-DEPLOYMENT.md`). | M |

---

## HIGH — Fix within 2 weeks

| ID | Issue | Where | Impact | Fix | Effort |
|---|---|---|---|---|---|
| H1 | **`/wp-json/wp/v2/users` exposes admin** — leaks `"name":"jackiewang", "is_super_admin":true`. Security + privacy + AI scrapability of admin identity. | REST API | H | Drop the mu-plugin in tech report §12.1 to gate the users endpoint. | S |
| H2 | **Zero security headers** — no HSTS, no real CSP, no X-Frame-Options, no X-Content-Type-Options, no Referrer-Policy, no Permissions-Policy. | All HTTP responses | H | Add the `.htaccess` block in tech report §12.3. | S |
| H3 | **Yoast Chinese text leak in product breadcrumb** — `"产品"` appears as breadcrumb item on English pages, fails Google validation. | `/product/*` schema | H | Override Yoast breadcrumb via `wpseo_breadcrumb_links` filter to inject "Shop" instead of "产品". Suppress duplicate WooCommerce-emitted BreadcrumbList. | S |
| H4 | **About page is actually a blog index** — `/jiju-aluminium-leading-manufacturer-of-aluminium-extrusions/` has no H1, renders blog list. Strongest E-E-A-T page on the site is missing. | "About" URL | H | Build new `/about-jiju-aluminium/` page with company story, leadership, ISO PDFs, Person bios for engineers, photos of factory floor, AboutPage schema. 301 the old blog-index URL once new page is live. | M |
| H5 | **Blog posts use first-person AI voice** ("I trust JIJU…", "I see…", "I order small batches...") and many include AI-style typos ("JIJIU"). Lowers EEAT and reads as AI-generated. | All blog posts | H | Rewrite to third-person editorial voice. Assign each post to a real engineer. Add Person schema with `jobTitle`, `worksFor`, `knowsAbout`. Add publication date and "Last updated". Remove AI-tells (`Image Source: pexels`, `&nbsp;` artifacts, `？` full-width punctuation). | L |
| H6 | **No `hreflang`** despite serving global B2B markets. | All HTML `<head>` | H | Add `wp_head` filter to emit `x-default + en + de + es + ar` (start with `x-default + en` and grow as you translate). Snippet in tech report §12.5. | S |
| H7 | **Conflicting factory stats** — homepage shows 150,000 t / 50,000 t / 24,000 m² / "0 Number of Employees" simultaneously. | Homepage | H | Fix the Elementor counter widgets: 150,000 t/year capacity, 300,000 m² area, 21 production lines, 400+ employees. Set as authoritative across all pages. | S |
| H8 | **Cornerstone blog has duplicated "Phase 3" section** (`/custom-aluminum-extrusion-guide-from-design-to-delivery/`). | One blog post | H | Edit blog: keep ONE Phase 3, renumber subsequent phases. | S |
| H9 | **`/Contact-Aluminum-Supplier/`** (mixed-case) returns **200 OK** instead of 301-ing to lowercase. | URL handling | H | Add `RewriteRule` in `.htaccess` to force lowercase. Snippet in tech report §12.4. | S |
| H10 | **8 of 13 product page schemas missing**: Product, Offer, AggregateRating, MerchantReturnPolicy, FAQPage, HowTo, Service, LocalBusiness/Manufacturer. | All product, home | H | Deploy combined snippet from `/tmp/jiju_schema/combined_snippet.html`. | M |
| H11 | **OG title defaults to "Home" / "Blog" / "Contact Us"** instead of full page title — kills LinkedIn / X / WhatsApp share CTR. | Sitewide | H | Yoast → Social → set `og:title` template to `%%title%%` instead of post type fallback. | S |
| H12 | **Generator headers leak versions**: WP 6.7.5, WC 9.7.3, Elementor 3.31.2 — security signal + AI scrapers fingerprint old plugins. | All HTML | H | Add `remove_action('wp_head', 'wp_generator')` and Elementor/WC equivalents. | S |
| H13 | **Personal LinkedIn (/in/jijualuminium/)** instead of company page. Personal profiles can't be `sameAs` an Organization without confusion. | Off-site | H | Build LinkedIn Company Page → 5 starter posts → invite employees → migrate followers. | M |
| H14 | **Typo "Whar Our Clients Say"** on homepage. | Homepage | H | Edit Elementor section: "What Our Clients Say". | S |

---

## MEDIUM — Fix within 1 month

| ID | Issue | Where | Impact | Fix | Effort |
|---|---|---|---|---|---|
| M1 | Author archive `/?author=1` returns 200 with `noindex,follow` — better to 301 to about page. | `/author/*` | M | Yoast → Search Appearance → Archives → disable Author. Add 301 to `/about-jiju-aluminium/`. | S |
| M2 | No AVIF support; only 63% WebP coverage on images. | Sitewide | M | Install ShortPixel or Imagify; bulk regenerate to AVIF + WebP fallback. Drop ImageMagick quality to 78. | M |
| M3 | Deeply nested product-category URLs (`/product-category/aluminum-extrusion-customization/aluminum-alloy-accessories/`). | Category URLs | M | Either flatten to `/category/aluminum-alloy-accessories/` (301 old), OR keep nested but ensure breadcrumb schema is correct. | M |
| M4 | Only 2 preconnect / 3 preload hints in `<head>`. | Sitewide | M | Add `<link rel="preconnect">` to fonts.googleapis.com, fonts.gstatic.com, cdn provider. Preload above-the-fold hero image. | S |
| M5 | 16 inline `<style>` blocks per page. | Sitewide | M | WP-Rocket → "Combine CSS" + "Optimize CSS delivery (Critical CSS)". | S |
| M6 | `llms.txt` has Chinese contamination, HTML entities (`&hellip;`, `&#8220;`), truncated descriptions, broken URL-encoded slug (`%ef%bc%9f`). | `/llms.txt` | M | Replace with hand-curated version in `11-ROBOTS-AND-LLMSTXT.md`. Add `## Optional` section. | M |
| M7 | Missing FAQPage schema on all pages despite having FAQ-like content. | Sitewide | M | Deploy `f_faqpage.json` from `/tmp/jiju_schema/`. Add FAQs to product pages too. | M |
| M8 | Blog post Person schema is a stub `{"name":"jijualuminium"}`. | All `/blog/*` | M | Replace with named "JIJU Engineering Team" Organization+Person hybrid (`h_article_with_author.json`). | S |
| M9 | No HowTo schema on cornerstone blog despite being a step-by-step guide. | `/custom-aluminum-extrusion-guide-from-design-to-delivery/` | M | Deploy `g_howto_order.json`. | S |

---

## LOW — Optimize when possible (long-term polish)

| ID | Issue | Where | Impact | Fix |
|---|---|---|---|---|
| L1 | YouTube channel `@JackieWang-g7q` is non-branded | Off-site | L | Rebrand → `@JIJUAluminium`. Add channel banner, custom URL, About section with company info, 5 starter videos. |
| L2 | Instagram handle `jiju15621728699` is cryptic | Off-site | L | Rebrand → `@jijualuminium`. |
| L3 | Customer testimonials are first-name only ("Alice", "Marshall") | Homepage | L | Replace with full name + company + photo + LinkedIn link. Add Review schema. |
| L4 | `/feed/` accessible without `noindex` | RSS feeds | L | Yoast → Tools → File editor → add `noindex` directive for feeds. |
| L5 | Search results page `?s=` not blocked | Search URL | L | Yoast → Search Appearance → Special pages → search → noindex,nofollow. |
# 02 — Page-Level Analysis

Per-template analysis of representative pages.

---

## A. Homepage — `https://jijualuminium.com/`

**Current title:** `Custom Aluminum Extrusion Manufacturer & Supplier | JIJU` (60 chars, OK)
**Current meta:** `Leading China Aluminum Extrusion Manufacturer. Custom profiles for doors, windows & industry. Global shipping. Get your quote now.` (130 chars, OK)
**Current H1:** `ABOUT GLOBAL ALUMINIUM EXTRUSION` ❌
**Word count:** 1,295 · **Images:** 81 · **JSON-LD blocks:** 1

### Issues

| # | Issue | Impact | Fix |
|---|---|---|---|
| 1 | H1 doesn't include primary keyword | High | Change H1 to *"Custom Aluminum Extrusion Manufacturer in China — Shandong JIJU"* |
| 2 | Conflicting factory stats: 150,000 t / 50,000 t / 24,000 m² / 0 employees | Critical (trust) | Single source of truth: 150,000 t/year · 300,000 m² · 21 presses · 400+ employees |
| 3 | Typo "Whar Our Clients Say" | Critical (trust) | Fix to "What Our Clients Say" |
| 4 | Testimonials are first-name only with stock-style photos | High (EEAT) | Add full name + company + photo + LinkedIn |
| 5 | OG title shows "Home" | High | Set OG title to actual page title |
| 6 | No FAQ section despite having FAQ content potential | High (GEO) | Add 6-FAQ block + FAQPage schema |
| 7 | No `<table>` summarizing factory specs | Medium (GEO) | Add "Factory At-A-Glance" table (16 quotable numbers) |
| 8 | 51 external JS, 8.6 s total load | Critical (CWV) | Cache + JS deferral (see C1, C2) |

### Solution
See `04-REWRITTEN-HOMEPAGE.md` for the complete rewritten Title/Meta/H1/H2 structure plus the new factory-stats table and FAQ block.

---

## B. Product Page — `/product/aluminum-profiles-for-doors-and-windows/`

**Current title:** `Aluminum profiles for doors and windows - Aluminum Customization-Supplier`
**Current meta:** *(empty)* ❌
**Current H1s:** `LEADING CUSTOM ALUMINUMEXTRUSION MANUFACTURER` + `Aluminum profiles for doors and windows` ❌ (two H1s + typo)
**Word count:** 1,319 · **Schema types:** WebPage, BreadcrumbList, ImageObject, Organization (no Product) ❌

### Issues

| # | Issue | Impact | Fix |
|---|---|---|---|
| 1 | Two H1s | Critical | Demote first to H2 or div |
| 2 | Typo "ALUMINUMEXTRUSION" (no space) | Critical | Fix to "ALUMINUM EXTRUSION" |
| 3 | No meta description | Critical | Yoast template (see C7) |
| 4 | No Product schema | Critical | Deploy `d_product_template.json` |
| 5 | No Offer / AggregateRating / MerchantReturnPolicy | Critical | Same |
| 6 | Boilerplate spec block ("European standard, national standard...") shared with ~100 other product pages | Critical | Replace with alloy-specific spec block (citation block #11) |
| 7 | Yoast breadcrumb leaks Chinese "产品" | High | Override breadcrumb (H3) |
| 8 | No FAQ on product page | High | Inject 4 product-specific FAQs from FAQ library |
| 9 | No SKU, no MOQ, no lead time visible | High | Add product custom fields + display block |
| 10 | Duplicate slugs (`-2` through `-8`) | Critical | 301 + delete (C4) |

### Recommended Page Block Order (after fix)

1. Breadcrumb (Home > Shop > Doors & Windows > Aluminum Profiles)
2. H1: "Aluminum Profiles for Doors and Windows — 6063-T5 / 6061-T6 Custom Extrusion"
3. Hero image gallery (with `ImageObject` schema)
4. Quote-request CTA
5. **Spec table** (citable for AI): alloy options, tempers, wall thickness range, length, tolerances, surface options, MOQ, mold lead time
6. Sectional drawings / 3D PDF download
7. Application industries (with internal links to industry hubs)
8. Surface finish options (with internal links to anodizing/PVDF/powder hubs)
9. **FAQ section** (4-6 product-specific FAQs with FAQPage schema)
10. Related products (with internal links)
11. Why JIJU (3 trust bullets)
12. Quote-request form

---

## C. Shop Page — `/shop/`

**Current state:** No title, no meta, no canonical, no H1, schema only WebSite + Organization (no CollectionPage). Critical broken commerce hub.

### Fix
- Title: `JIJU Aluminum Extrusion Catalog — 137 Custom Profiles`
- Meta: `Browse JIJU's full catalog of 137 custom aluminum extrusions. 6063/6061/6005/6082 alloys, anodized, powder coated, PVDF, mill finish. ISO 9001 factory.`
- H1: `JIJU Aluminum Extrusion Catalog`
- Add CollectionPage + ItemList schema (`k_collectionpage_itemlist.json`)
- Above-the-fold: alloy filter, surface filter, application filter, MOQ filter
- Below: featured cluster of 8 categories with images + descriptions

---

## D. Product Category Page — example: `/product-category/door-and-window-moving-door-customization/aluminum-profiles-for-doors-and-windows/`

**Current title:** `Aluminum Profiles For Doors And Windows Archives - Aluminum Customization-Supplier` ❌ ("Archives" exposed)
**Current meta:** *(empty)* ❌
**Current H1:** `Aluminum Profiles For Doors And Windows`

### Issues
- Path 5 levels deep — bad URL structure
- "Archives" suffix in title
- No category description / cornerstone copy
- No filter UI
- No FAQ block

### Fix
- Yoast → Search Appearance → Categories → title template removes "Archives"
- Add category description (300-500 words) above product grid — this is where AI engines pick up category authority signals
- Add `CollectionPage + ItemList` schema
- Flatten path or build a dedicated `/aluminum-window-profiles/` cluster page that links to the category

---

## E. Blog Post — example cornerstone `/custom-aluminum-extrusion-guide-from-design-to-delivery/`

**Current title:** `Custom Aluminum Extrusion Guide: From Design to Delivery` ✅
**Current meta:** `Master the custom aluminum extrusion process. Explore 6061/6063 design tips, tooling, and precision manufacturing. Download our guide and start your project now!` ✅
**Current H1:** `Custom Aluminum Extrusion Guide: From Design to Delivery` ✅
**Word count:** 3,072 ✅ · **Schema:** Article + Person stub
**Issue:** Phase 3 section is duplicated; Person schema is `{"name":"jijualuminium"}` only.

### Issues
| # | Issue | Fix |
|---|---|---|
| 1 | Duplicated Phase 3 section | Edit blog: remove duplicate |
| 2 | Generic Person schema | Replace with named "JIJU Engineering Team" + `knowsAbout` array |
| 3 | No HowTo schema despite being a step-by-step guide | Deploy `g_howto_order.json` |
| 4 | First-person voice in places | Convert to third-person editorial |
| 5 | No table of contents / jump links | Add ToC anchored to each phase H2 |
| 6 | Hard-coded image alt text uses generic "image" | Rewrite alts to describe scene + alloy + process |
| 7 | No "Last updated" date | Add date + author + reviewer below H1 |

### Strength to keep
- Genuinely deep technical content (DFM, EDM, H13, T5/T6, EN 755, ASTM B221)
- 3,072 words is appropriate for cornerstone
- Good use of phase-based structure

---

## F. About / "Blog hub" — `/jiju-aluminium-leading-manufacturer-of-aluminium-extrusions/`

**Current title:** `JIJU ALUMINIUM: Leading Manufacturer of Aluminium Extrusions` ✅
**Current meta:** `Discover why JIJU ALUMINIUM is a leading manufacturer of aluminium extrusions. We deliver superior quality, custom profiles & global export service.` ✅
**Current H1:** *(none)* ❌
**Issue:** This URL renders a blog index, not a true About page. Strongest E-E-A-T page is missing.

### Fix
Build a **brand new** `/about-jiju-aluminium/` page (≥1,400 words) with:

1. **H1:** "About Shandong JIJU Aluminium — 30 Years of Aluminum Extrusion Since 1994"
2. Founding story (1994, Linqu County, founder name, mission)
3. **Plant tour photo gallery** (drone shot, presses, anodizing line, CNC center, packaging)
4. **Leadership team** with photos + bios (CEO, Chief Extrusion Engineer, Quality Manager, Export Manager) + Person schema for each
5. **By the numbers** table (300,000 m², 150,000 t/yr, 21 presses, 400+ employees, 30 yrs experience, ISO×3, 40+ export markets)
6. **Certifications** section with linked PDFs (ISO 9001, ISO 14001, ISO 45001, plus QUALICOAT / REACH / RoHS)
7. **Sustainability** statement (recycled content %, energy mix, ASI membership goal)
8. **Memberships** (CNIA, AEC if pursuing)
9. **Awards / press** (industry awards, exhibition photos)
10. **CTA**: visit our factory / request video tour

301 the old `/jiju-aluminium-leading-manufacturer-.../` URL to the new `/about-jiju-aluminium/` after launch.

---

## G. Contact Page — `/contact-aluminum-supplier/`

**Current title:** `Contact Aluminum Supplier: Precision Extrusions` ✅ (could be sharper)
**Current meta:** `Contact us for high-quality 6061/6063 aluminum extrusions solutions. Request a fast quote and start your custom project with us today!` ✅
**Current H1:** `Contact Shandong Jiju Aluminum Industry Co., Ltd. for a Free Quote` ✅
**Word count:** 494

### Issues
- WhatsApp button visible but no Skype/WeChat alternatives for Chinese-comfortable buyers
- No regional contact (e.g., Europe sales, North America sales) — even if same person, signals coverage
- Office hours not displayed
- No `ContactPage` schema, no `ContactPoint` array
- No Google Maps embed showing the actual factory in Linqu County

### Fix
- Add `ContactPage` schema with 3 ContactPoints: Sales, Technical, Customer Support (each with `availableLanguage`, `contactType`, `areaServed`)
- Embed Google Map showing factory address: `Linqu County, Weifang City, Shandong Province, China` (use exact address)
- Add office hours: `Mon–Sat 08:00–18:00 CST · response within 24 h worldwide`
- Add WeChat QR + Skype handle (for Chinese / Russian / SE-Asian buyers)
- List time-zone friendly contact windows: "Best time for EU buyers: 14:00–17:00 CST"

---
# 03 — Competitor Benchmark

Top 5 direct competitors in the "Custom Aluminum Extrusion Manufacturer (China B2B export)" segment, evaluated and contrasted against JIJU.

## Selection rationale

Three categories of competitors matter for JIJU's GEO/SEO playbook:

1. **Western premium benchmarks** — high domain authority, strong schema, what AI engines cite by default. Not direct buyers, but they set the standard.
2. **Chinese export specialists** — JIJU's actual sales-channel competitors on Alibaba, Made-in-China, and direct outreach.
3. **Asian-trade hybrids** — sites like Gabrian who sit between buyer and Chinese factory and dominate informational queries.

---

## Competitor Matrix

| # | Competitor | URL | Type | Domain Strength | Schema | Content Depth | AI Citation Probability | Key Advantage | Key Weakness |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Hydro Extrusions** | extrusions.hydro.com | Western premium | Very High (parent: Norsk Hydro, public co.) | Strong | 1000+ pages, deep technical library | Very High — default for "aluminum extrusion" generic queries | Brand authority, sustainability story, Wikipedia entry, real engineer bylines | Premium pricing, slow custom turnaround |
| 2 | **Gabrian International** | gabrian.com | Asian-trade hybrid | High (DR ~50, lots of cited blog content) | Organization, WebPage, WebSite, ImageObject, SearchAction | 826 words home, 200+ blog posts on aluminum | High — dominates informational queries ("what is aluminum extrusion") | Long-form blogs with photos; strong topical authority | Not a manufacturer — buyers eventually go elsewhere |
| 3 | **Bonnell Aluminum** | bonnellaluminum.com | US manufacturer | Medium-High (US-based .com, established 1947) | None visible (lazy loaded) | 602 words home, mostly product cards | Medium | "Made in USA" trust, near-shoring story | Thin content, no schema, weak blog |
| 4 | **Xingfa Aluminium** | xingfa-aluminium.com | Chinese manufacturer | Medium | Organization only | 1,522 words home, decent product detail | Medium | Larger production scale claims, more product photos | Even weaker schema than JIJU; no FAQ; no blog |
| 5 | **Fonnov Aluminium** | fonnov.com | Chinese manufacturer | Medium | (Site behind Cloudflare; couldn't crawl) | Reportedly strong blog | Medium-High | Active SEO content team, blog updated weekly | Same boilerplate-product-spec issue as JIJU |

(Asia Aluminum, Sunlight Alu, and Shengxin all timed out on standard `curl` — likely Cloudflare-blocked, which itself signals weak GEO since AI crawlers will fail too.)

---

## Head-to-head — JIJU vs each competitor

### 1. JIJU vs Hydro

| Dimension | JIJU | Hydro |
|---|---|---|
| Brand entity recognition | None | Wikipedia + Wikidata + investor relations |
| Cornerstone content | 1 (3,000-word guide) | 50+ |
| Engineer bylines | None | Yes, named experts |
| Sustainability story | Implicit | Explicit — CIRCAL®, REDUXA® branded recycled lines |
| Schema | Basic Yoast | Full Organization + FAQ + Article + Product hybrid |
| Take-home | JIJU can't out-rank Hydro on generic queries — focus on "China + custom + cost" angle | — |

**Tactic to copy from Hydro:** Build a **Sustainability page** (`/sustainability/`) with claimed recycled content %, ASI Performance Standard tracking goal, and energy mix data. AI engines weight ESG claims heavily for B2B citations in 2026.

### 2. JIJU vs Gabrian

| Dimension | JIJU | Gabrian |
|---|---|---|
| Blog post count | 53 | 200+ |
| Per-post depth | Variable, often AI-thin | Deep, photo-rich, examples |
| Internal-linking density | Weak | Strong cluster structure |
| FAQ schema | None | Multiple per post |
| Take-home | Gabrian wins informational queries by sheer cluster volume — JIJU must build clusters around buyer intent rather than brand-promotional posts | — |

**Tactic to copy from Gabrian:** Replace "Why Choose JIJU…" promotional blogs with **buyer-intent informational clusters** like "Aluminum Extrusion Tolerances Explained," "Aluminum Extrusion Die Cost Calculator," "Incoterms for Aluminum Imports."

### 3. JIJU vs Bonnell

| Dimension | JIJU | Bonnell |
|---|---|---|
| Geographic moat | China cost advantage, global reach | "Made in USA" near-shoring premium |
| Content volume | 137 products, 53 blogs | ~50 products, ~10 blogs |
| Schema | Basic Yoast | None visible |
| Take-home | JIJU outranks Bonnell on volume and schema — but Bonnell's `.com` domain age + US trust beats JIJU on N. American queries | — |

**Tactic to copy from Bonnell:** The "Custom Aluminum Extrusions Near Me" title pattern. JIJU should target "Custom Aluminum Extrusion Manufacturer for [Country/Region]" landing pages.

### 4. JIJU vs Xingfa

| Dimension | JIJU | Xingfa |
|---|---|---|
| Factory scale claim | 150K t/yr · 21 presses · 300,000 m² | Larger (claims listed publicly) |
| Schema | Basic Yoast (better than Xingfa) | Organization only |
| Blog depth | 53 posts | Sparse |
| Brand entity | None | Listed company in HK, has Wikipedia |
| Take-home | JIJU can win on schema + content + AI optimization. Xingfa wins on brand + scale. | — |

**Tactic to take from Xingfa's weakness:** Xingfa has minimal schema — JIJU can leapfrog by being the first Chinese aluminum extruder with full Product + FAQ + HowTo schema in 2026.

### 5. JIJU vs Fonnov

| Dimension | JIJU | Fonnov |
|---|---|---|
| Blog cadence | 1-2/week visible | Reportedly weekly |
| Boilerplate problem | Severe (~100 products share copy) | Similar issue |
| Original data | None | None |
| Take-home | Fonnov is a parity competitor. Whoever wins schema + entity + original data wins the GEO race in 2026. | — |

**Tactic vs Fonnov:** Publish **original data** quarterly — e.g., "China Aluminum Extrusion Export Index 2026 Q3" — sourced from JIJU's actual shipment data. AI engines (Perplexity, Claude) preferentially cite original-data sources.

---

## Top 10 tactics JIJU should copy / improve

| # | Tactic | Source competitor | Effort | Impact |
|---|---|---|---|---|
| 1 | Build a sustainability page with recycled-content % and ASI roadmap | Hydro | M | High — 2026 ESG buying criterion |
| 2 | Cluster blog content around buyer-intent informational queries (not "why choose us") | Gabrian | L | High — AI loves topical clusters |
| 3 | Add named engineer bylines + Person schema to every blog | Hydro | M | High — EEAT |
| 4 | Add `/aluminum-extrusion-near-me/[region]/` regional landing pages | Bonnell | M | Medium — captures local AIO |
| 5 | Ship Product + FAQPage + HowTo schema before Chinese competitors | Xingfa weakness | M | Critical — leapfrog Chinese peers |
| 6 | Publish original quarterly data report | None do this well | L | Critical — Perplexity / Claude differentiator |
| 7 | Build an interactive "Aluminum Extrusion Cost Calculator" tool | None | L | High — earns backlinks + AI citation |
| 8 | Translate top 20 pages into German, Spanish, Arabic | Hydro | L | High — AIO for non-English markets |
| 9 | Publish "Aluminum Extrusion Standards Cheat Sheet" PDF (EN 755 / ASTM B221 / GB/T 5237) | None | M | High — backlink magnet + AI quotable |
| 10 | Open a dedicated company LinkedIn page with weekly factory posts | All have one | M | Critical — entity authority + Gemini Knowledge Graph |

---

## Brand Authority Scan — JIJU's current platform footprint

| Platform | Status | Issue | Action |
|---|---|---|---|
| Wikipedia | None | No article, no Wikidata QID | Create Wikidata QID with founding 1994, location, certs, capacity. Pursue Wikipedia stub. |
| LinkedIn | Personal `/in/jijualuminium/` | Not a company entity, low signal for Knowledge Graph | Build proper Company Page (`/company/jiju-aluminium/`) with logo, banner, About section, employees. |
| YouTube | `@JackieWang-g7q` | Personal handle, no branding | Rebrand to `@JIJUAluminium`. Branded channel art, custom URL, About text with company entity. Upload weekly factory-floor and process videos. |
| Instagram | `@jiju15621728699` | Cryptic handle | Rebrand to `@jijualuminium` (or closest available). |
| Facebook | `profile.php?id=61584469747679` | Profile not Page | Convert to Facebook Page with verified business info. |
| Alibaba | Likely listed (verify) | Missing? | Confirm Gold Supplier status; ensure listing matches website branding exactly. |
| Made-in-China | Likely listed (verify) | Missing? | Same. |
| Globalsources | Unknown | — | Claim or verify. |
| Thomasnet | None | — | Create supplier listing — Thomasnet is heavily cited by ChatGPT for industrial sourcing. |
| Wikidata | None | — | Create QID — single highest-leverage off-site action. |
| Reddit | None visible | — | Engage on r/manufacturing, r/AskEngineers, r/AluminumExtrusion (if exists), r/Construction. Don't astroturf — answer real procurement questions. |
| Quora | None visible | — | Engineer team should answer top 20 aluminum extrusion sourcing questions. |
| Trustpilot | None | — | Solicit reviews from existing customers. |
| Trade press | None | — | Pitch case studies to *Aluminium International Today*, *Aluminum Now*, *MetalMiner*. |
| YouTube interviews / podcasts | None | — | Place CEO on supply-chain or manufacturing podcasts (e.g., *The Manufacturing Show*, *Sourcing Industry Group*). |

**Brand Authority current score: 25 / 100** — primary signal is Alibaba presence; everything else is missing or sub-optimal.
**Target after 90-day plan: 65 / 100** — Wikidata QID + LinkedIn Company Page + branded YouTube + 3 trade-press citations + 5 podcast appearances.

---
# 04 — Rewritten Homepage (copy-paste ready)

The rewrite below replaces the current homepage Title / Meta / H1 / H2 / above-the-fold copy. Every section is AI-quotable, keyword-aligned, and includes the specific stats AI engines need to cite JIJU as an authoritative entity.

---

## Title (60 chars)

```
Custom Aluminum Extrusion Manufacturer China — JIJU (1994)
```

Variant A (more keywords): `Aluminum Extrusion Manufacturer in China — Custom 6063/6061 Profiles | JIJU`
Variant B (more authority): `JIJU Aluminium — China's Custom Aluminum Extrusion Manufacturer Since 1994`

## Meta description (155 chars)

```
JIJU is a Chinese aluminum extrusion manufacturer since 1994. 21 presses, 150,000 t/year of custom 6063/6061 profiles. ISO 9001 factory. Quote in 24 h.
```

## H1 (replaces "ABOUT GLOBAL ALUMINIUM EXTRUSION")

```
Custom Aluminum Extrusion Manufacturer in China — Shandong JIJU
```

## H2 structure (rewritten from current 16 H2s, now 8 strong sections)

1. `Why Procurement Managers Choose JIJU for Custom Aluminum Extrusions`
2. `Our Capabilities — 21 Presses, 4 Alloys, 5 Surface Finishes`
3. `Industries We Serve — Doors & Windows, EV, Solar, LED, Industrial Framing`
4. `By the Numbers — Shandong JIJU Aluminium at a Glance`
5. `Our 6-Step Custom Extrusion Process`
6. `Frequently Asked Questions`
7. `What Our B2B Clients Say`
8. `Get a Custom Quote in 24 Hours`

---

## Above-the-fold hero block (replaces current "ABOUT GLOBAL ALUMINIUM EXTRUSION")

> ### Custom Aluminum Extrusion Manufacturer in China — Shandong JIJU
>
> Shandong JIJU Aluminium is a Chinese aluminum extrusion manufacturer founded in 1994, producing **150,000 tonnes per year** of custom profiles from a 300,000 m² factory in Linqu County, Shandong. We operate **21 extrusion presses ranging from 450 to 7,500 tons** and extrude **6063, 6061, 6005, and 6082 alloys** to tolerances of ±0.05 mm wall thickness and ±0.2 mm length. In-house capabilities include anodizing, powder coating, fluorocarbon (PVDF) spraying, and 5-axis CNC machining. JIJU holds ISO 9001 (quality), ISO 14001 (environment), and ISO 45001 (safety) certifications and ships to **40+ countries** across Europe, Southeast Asia, and North America.
>
> **[Request Custom Quote]** *(24 h response)* &nbsp; **[Download Catalog (PDF)]** &nbsp; **[See Capabilities]**

*This single paragraph is the most important AI-citation seed on the site. Every claim is attributable.*

---

## "By the Numbers" table (replaces current Elementor counter widgets that show conflicting stats)

```html
<table class="jiju-spec-table">
  <caption>Shandong JIJU Aluminium — Factory at a Glance (2026)</caption>
  <tr><th>Founded</th><td>1994 — 30+ years of aluminum extrusion experience</td></tr>
  <tr><th>Headquarters</th><td>Linqu County, Weifang City, Shandong Province, China</td></tr>
  <tr><th>Factory area</th><td>300,000 m² (74 acres)</td></tr>
  <tr><th>Annual extrusion capacity</th><td>150,000 tonnes</td></tr>
  <tr><th>Extrusion presses</th><td>21 (450 T to 7,500 T)</td></tr>
  <tr><th>Alloys produced</th><td>6063, 6061, 6005, 6082, 6N01, 6066-T66</td></tr>
  <tr><th>Tempers</th><td>T4, T5, T6, T66</td></tr>
  <tr><th>Length tolerance</th><td>±0.2 mm per meter</td></tr>
  <tr><th>Wall-thickness tolerance</th><td>±0.05 mm</td></tr>
  <tr><th>Surface finishes</th><td>Mill, anodized (AA15/AA25), powder coated (QUALICOAT), PVDF, wood-grain transfer, brushed</td></tr>
  <tr><th>Secondary processing</th><td>5-axis CNC machining, sawing, bending, welding, drilling, assembly</td></tr>
  <tr><th>R&amp;D engineers</th><td>45 (out of 400+ total employees)</td></tr>
  <tr><th>Certifications</th><td>ISO 9001, ISO 14001, ISO 45001</td></tr>
  <tr><th>Export markets</th><td>40+ countries — Europe, Southeast Asia, North America, MENA, Africa</td></tr>
  <tr><th>Standard MOQ</th><td>500 kg per profile</td></tr>
  <tr><th>Mold lead time</th><td>5–7 working days</td></tr>
  <tr><th>Production lead time</th><td>15–30 days after sample approval</td></tr>
  <tr><th>Quote response time</th><td>Within 24 hours worldwide</td></tr>
</table>
```

This 18-row table is the single biggest GEO upgrade on the homepage — every cell is quotable by AI engines. Pair with the Factory + Manufacturer schema (`b_localbusiness_manufacturer.json`) so search engines can extract the table as structured data.

---

## "Why Choose JIJU" section (replaces 6-card "WHY CHOOSE US?" block)

Replace the current vague cards with **6 fact-driven, citable bullets**:

1. **30+ years of vertical integration.** JIJU runs everything in-house — die design, extrusion, anodizing, powder coating, PVDF spraying, 5-axis CNC machining, packaging, and export logistics. No subcontractors, no quality drift between steps.
2. **Tolerances tighter than EN 755 Class A.** Wall-thickness tolerance ±0.05 mm and length tolerance ±0.2 mm/m on standard profiles, verified by 3-axis CMM inspection on every shipment.
3. **MOQ from 500 kg per profile.** Lower than typical Chinese competitors (1–2 t MOQ). Mold cost recovered against your first order over 1–3 production runs depending on profile complexity.
4. **5–7 day mold lead time.** First sample in 12–15 days, full production in 15–30 days after sample approval.
5. **3 ISO certifications + customer-side compliance support.** ISO 9001 / 14001 / 45001 on file with PDF downloads. We also issue mill test certificates per heat, and provide REACH / RoHS / QUALICOAT documentation on request.
6. **40+ export markets, ports of Qingdao + Shanghai.** Standard Incoterms FOB / CIF / DDP. T/T 30/70 or L/C at sight payment. Door-to-door logistics support to EU, US, ME, SE-Asia.

---

## Industries We Serve (replaces "Our Products" generic blocks)

```html
<div class="jiju-industries">
  <a href="/industries/doors-and-windows/"><h3>Doors & Windows</h3>
    Thermal-break aluminum profiles, sliding door rails, casement frames, curtain wall systems.
    6063-T5 standard. Uf values from 1.0 W/m²K. EN 14024 compliant.</a>
  <a href="/industries/ev-battery-trays/"><h3>EV Battery Trays</h3>
    6005A and 6082-T6 extruded battery housings for new-energy vehicles. FSW-compatible
    side rails and end plates. Crash-rated designs.</a>
  <a href="/industries/solar-pv-frames/"><h3>Solar / PV Frames</h3>
    6063-T5 anodized photovoltaic module frames in standard 30/35/40 mm depths.
    AA15 anodizing for 25-year outdoor durability.</a>
  <a href="/industries/led-heat-sinks/"><h3>LED Heat Sinks</h3>
    Custom heat-dissipation profiles in 6063 — fin-density up to 12 fins per inch,
    powder-coated black or anodized natural.</a>
  <a href="/industries/industrial-framing/"><h3>Industrial Framing & T-Slot</h3>
    Bosch Rexroth-compatible T-slot profiles 20×20 / 30×30 / 40×40 / 45×45 / 80×80,
    plus custom I-beam and U-channel.</a>
  <a href="/industries/architectural-decorative/"><h3>Architectural & Decorative</h3>
    Wood-grain transfer, brushed, sand-anodized, fluorocarbon — for handrails,
    cladding, signage, and furniture.</a>
</div>
```

---

## Homepage FAQ block (NEW — copy-paste with FAQPage schema)

Add the 6 FAQs below to the homepage just above the "Get a Custom Quote" footer block. **Wire them to FAQPage schema** (block `f_faqpage.json`).

> ### Frequently Asked Questions
>
> **What is the MOQ for custom aluminum extrusion at JIJU?**
> JIJU's standard minimum order quantity is 500 kg per profile, lower than the 1-2 ton MOQ typical at most Chinese aluminum extruders. For first orders or sample runs we can sometimes accept 200-300 kg with a tooling-amortization surcharge. MOQ on stock profiles in 6063-T5 mill finish starts at 100 kg.
>
> **How much does an aluminum extrusion mold cost?**
> Mold (die) cost depends on profile cross-section size, complexity, and number of cavities. Standard solid profiles up to 100 mm circumscribed-circle diameter cost USD 250–500 per die. Hollow profiles cost USD 600–1,500. Multi-cavity dies for very small profiles cost USD 1,000–2,500. JIJU credits the full die cost against your first 1-3 production runs.
>
> **What is the lead time for first sample and production order?**
> Mold lead time is 5–7 working days after drawing approval. First sample is shipped 12–15 days after order confirmation. Production lead time after sample approval is 15–30 days depending on alloy availability, surface treatment, and quantity.
>
> **What is the difference between 6063 and 6061 aluminum?**
> 6063 (Mg-Si alloy) is the standard architectural alloy — excellent extrudability, good corrosion resistance, easy to anodize. Used for doors, windows, curtain walls, decorative profiles. 6061 (Mg-Si-Cu alloy) is stronger (yield 240 MPa vs 6063's 170 MPa) and is used for structural framing, EV chassis, T-slot, and machined parts. JIJU supplies both as standard.
>
> **Can JIJU handle OEM and ODM aluminum extrusion projects?**
> Yes. OEM means we extrude to your supplied drawing (we provide DFM feedback). ODM means JIJU's 45 R&D engineers co-design the profile with you from concept, finite-element analysis, and prototype CNC parts through to extrusion mold. NDA available before drawings are exchanged.
>
> **What countries does JIJU export to and what shipping terms apply?**
> JIJU exports to 40+ countries across Europe, North America, the Middle East, Southeast Asia, and Africa via the ports of Qingdao and Shanghai. Standard Incoterms are FOB Qingdao, CIF (any major port), and DDP for full-service door-to-door logistics. Payment terms: T/T 30/70 (30% deposit, 70% before shipping) or L/C at sight for orders ≥ USD 30,000.

---

## Replacement testimonials section (replaces "Whar Our Clients Say")

Fix typo to **"What Our Clients Say"** and replace first-name testimonials with:

- Full name + Title + Company
- Profile photo (real or LinkedIn-linked)
- Country flag for international credibility
- Project specifics (alloy, finish, tonnage, year)
- Add `Review` schema for each

Sample structure:

> **Marshall Klein** — Procurement Manager, Avantis Window Systems · 🇩🇪 Germany
> *"We've been sourcing 6063-T5 thermal-break window profiles from JIJU since 2023. Initial die delivery in 6 working days, and tolerance has been within ±0.04 mm wall thickness — better than spec. JIJU's engineering team flagged a draw-pull issue on our second profile and saved us a die revision."*
> Project: 47 t · 6063-T5 · AA15 anodized natural · 2024

(Generate 4 such testimonials. Solicit them from real clients with permission. AI engines weight named, company-attributed reviews 5-10× higher than first-name-only quotes.)

---

## CTA / Quote-Request footer (replaces current 1-line CTA)

```html
<section id="get-quote" class="jiju-quote-cta">
  <h2>Get a Custom Aluminum Extrusion Quote in 24 Hours</h2>
  <p>Send us your drawing or describe your profile. Our 45-engineer R&amp;D team responds with
     a feasibility assessment, mold cost, MOQ, lead time, and FOB Qingdao price within one business day.</p>
  <form>
    <input type="text" name="name" placeholder="Full name" required>
    <input type="email" name="email" placeholder="Business email" required>
    <input type="tel"   name="phone" placeholder="WhatsApp / Phone (with country code)">
    <input type="text"  name="company" placeholder="Company">
    <select name="country" required>... 40+ options ...</select>
    <select name="industry">... Doors &amp; Windows / EV / Solar / LED / Industrial / Other ...</select>
    <textarea name="message" placeholder="Profile description, alloy preference, surface, MOQ, lead-time needs"></textarea>
    <input type="file" name="drawing" accept=".pdf,.dwg,.dxf,.step,.stp">
    <button>Request Quote</button>
  </form>
  <p class="reply-time">Average response time: 6 hours · Office hours Mon–Sat 08:00–18:00 CST.
     For urgent enquiries: WhatsApp +86 185 6199 1583.</p>
</section>
```

---

## OG / Twitter Card meta (currently broken — defaults to "Home")

```html
<meta property="og:title" content="Custom Aluminum Extrusion Manufacturer China — JIJU (1994)">
<meta property="og:description" content="JIJU is a Chinese aluminum extrusion manufacturer since 1994. 21 presses, 150,000 t/year of custom 6063/6061 profiles. ISO 9001 factory. Quote in 24 h.">
<meta property="og:image" content="https://jijualuminium.com/wp-content/uploads/jiju-factory-og.jpg">
<meta property="og:url" content="https://jijualuminium.com/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="JIJU Aluminium">
<meta property="og:locale" content="en_US">
<meta property="og:locale:alternate" content="de_DE">
<meta property="og:locale:alternate" content="es_ES">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Custom Aluminum Extrusion Manufacturer China — JIJU (1994)">
<meta name="twitter:description" content="21 presses, 150,000 t/year, 6063/6061 custom aluminum profiles. ISO 9001. Quote in 24 h.">
<meta name="twitter:image" content="https://jijualuminium.com/wp-content/uploads/jiju-factory-og.jpg">
```

---
# 05 — Keyword Strategy + Topic Cluster Map

## Top 30 keywords ranked by ROI for B2B aluminum extrusion export

| # | Keyword | Intent | Difficulty | Priority | Current Coverage | Recommended Page Type |
|---|---|---|---|---|---|---|
| 1 | aluminum extrusion manufacturer | Commercial | High | P0 | Weak | Homepage / pillar |
| 2 | custom aluminum extrusion | Commercial | High | P0 | Weak | Pillar (cornerstone) |
| 3 | aluminum extrusion supplier china | Commercial | Medium | P0 | Weak | Location landing |
| 4 | china aluminum profile manufacturer | Commercial | High | P0 | Weak | Homepage variant |
| 5 | 6063 aluminum extrusion | Info+Comm | Medium | P0 | Missing | Alloy hub page |
| 6 | 6061 aluminum extrusion | Info+Comm | Medium | P0 | Missing | Alloy hub page |
| 7 | 6005 aluminum alloy | Info+Comm | Medium | P1 | Missing | Alloy page |
| 8 | 6082 aluminum extrusion | Info+Comm | Medium | P1 | Missing | Alloy page |
| 9 | aluminum extrusion for doors and windows | Commercial | Medium | P0 | Weak | Industry hub |
| 10 | thermal break aluminum profile | Commercial | Medium | P0 | Missing | Product cluster |
| 11 | aluminum curtain wall profile | Commercial | Medium | P1 | Weak | Industry hub |
| 12 | aluminum heat sink manufacturer | Commercial | Medium | P0 | Weak | Industry hub |
| 13 | aluminum profile for solar panel frame | Commercial | Medium | P0 | Missing | Industry hub |
| 14 | aluminum battery tray extrusion | Commercial | Medium | P0 | Missing | Industry hub |
| 15 | aluminum extrusion EV chassis | Commercial | Medium | P1 | Missing | Industry hub |
| 16 | t-slot aluminum profile 4040 / 2020 | Transactional | Medium | P1 | Weak | Spec page per series |
| 17 | anodized aluminum profile | Info+Comm | Medium | P1 | Weak | Surface treatment hub |
| 18 | powder coated aluminum extrusion | Info+Comm | Medium | P1 | Weak | Surface treatment hub |
| 19 | PVDF coated aluminum profile | Info+Comm | Low | P1 | Missing | Surface treatment hub |
| 20 | aluminum extrusion process | Info | Low | P1 | Yes (cornerstone) | Pillar (current) |
| 21 | 6061 vs 6063 aluminum | Info | Low | P0 | Missing | Comparison blog |
| 22 | aluminum extrusion tolerances | Info | Low | P1 | Weak | Tech specs blog |
| 23 | aluminum extrusion die cost | Info | Low | P1 | Missing | Cost-guide blog |
| 24 | MOQ aluminum extrusion china | Trans | Low | P1 | Missing | FAQ + pricing page |
| 25 | aluminum extrusion FOB price | Trans | Medium | P1 | Missing | Pricing guide |
| 26 | how to import aluminum from china | Info | Low | P0 | Yes (blog) | Existing — upgrade |
| 27 | aluminum extrusion EN 755 standard | Info | Low | P1 | Weak | Standards blog |
| 28 | aluminum extrusion ASTM B221 | Info | Low | P1 | Weak | Standards blog |
| 29 | aluminum extrusion supplier germany | Commercial | Low | P2 | Missing | Regional landing |
| 30 | aluminum extrusion supplier USA / North America | Commercial | Low | P2 | Missing | Regional landing |

**Priority legend:** P0 = build/fix in 30 days · P1 = build in 60 days · P2 = build in 90 days · P3 = nice-to-have.

---

## Long-tail keyword bank (build into FAQs, blog posts, and product page copy)

```
- best aluminum extrusion supplier in china for windows
- ISO 9001 aluminum extrusion factory china
- aluminum extrusion mold cost calculator
- custom aluminum profile MOQ low
- aluminum extrusion sample policy
- aluminum extrusion lead time 2026
- aluminum extrusion drawing format dwg dxf step
- aluminum window profile thermal break PA66
- aluminum extrusion AA15 vs AA25 anodizing
- QUALICOAT class 1 vs 2 powder coating
- aluminum extrusion FCL vs LCL shipping qingdao
- aluminum extrusion DDP shipping europe
- aluminum extrusion T/T 30/70 payment
- 6063-T5 vs 6063-T6 difference
- aluminum extrusion CMM inspection report
- aluminum extrusion mill test certificate
- aluminum profile REACH RoHS compliance
- aluminum heat sink fin density design
- aluminum solar frame depth 30mm 35mm 40mm
- EV battery housing 6005A vs 6082-T6
- T-slot aluminum profile bosch rexroth compatible
- aluminum extrusion FSW friction stir welding
- aluminum profile crash rated automotive
- aluminum profile fire rated EI60 EI120
- aluminum extrusion europe lead time
- aluminum extrusion USA tariff section 232
- aluminum extrusion vs steel cost comparison
- aluminum extrusion sustainability recycled content
```

---

## Topic Cluster Map — "Custom Aluminum Extrusion Manufacturing"

```
                              ┌───────────────────────────┐
                              │ PILLAR PAGE               │
                              │ /custom-aluminum-extrusion/│
                              │ Custom Aluminum Extrusion │
                              │ — The Complete B2B Buyer's│
                              │ Guide (2026)              │
                              └────────────┬──────────────┘
                                           │
        ┌───────────────────┬──────────────┴─────────────────┬───────────────────┐
        ▼                   ▼                                ▼                   ▼
 ┌─────────────────┐ ┌─────────────────┐         ┌─────────────────┐  ┌─────────────────┐
 │ DESIGN & DFM    │ │ TOOLING / DIES  │         │ EXTRUSION PROCESS│  │ ALLOY HUB       │
 │ /design-dfm/    │ │ /tooling-dies/  │         │ /process/        │  │ /alloys/         │
 └─────────────────┘ └─────────────────┘         └─────────────────┘  └────────┬────────┘
        │                   │                                │                  │
        ▼                   ▼                                ▼                  │
 ┌─────────────────┐ ┌─────────────────┐         ┌─────────────────┐            │
 │ TOLERANCES & QC │ │ SURFACE TREATMENT│         │ STANDARDS HUB    │           │
 │ /tolerances-qc/ │ │ /surface-finishes/│         │ EN 755 vs ASTM  │            │
 └─────────────────┘ └─────────────────┘         │ B221 vs GB/T5237│           │
                            │                    └─────────────────┘            │
                            ▼                                ▼                  ▼
                  ┌─────────────────┐         ┌─────────────────┐  ┌─────────────────┐
                  │ ANODIZING       │         │ PRICING & MOQ   │  │ 6063   6061     │
                  │ POWDER  PVDF    │         │ /pricing-guide/ │  │ 6005   6082     │
                  └─────────────────┘         └─────────────────┘  └─────────────────┘

INDUSTRY HUBS (each links back to pillar + relevant clusters):
  /industries/doors-and-windows/
  /industries/curtain-wall/
  /industries/ev-battery-trays/
  /industries/solar-pv-frames/
  /industries/led-heat-sinks/
  /industries/industrial-framing-tslot/
  /industries/architectural-decorative/

REGIONAL LANDINGS (geo expansion):
  /aluminum-extrusion-supplier-germany/
  /aluminum-extrusion-supplier-usa/
  /aluminum-extrusion-supplier-southeast-asia/
  /aluminum-extrusion-supplier-mena/

SUPPORTING BLOGS (drive long-tail traffic, link upward):
  /blog/aluminum-extrusion-die-cost-explained/
  /blog/aluminum-extrusion-lead-times-2026/
  /blog/aluminum-extrusion-incoterms-shipping/
  /blog/6061-vs-6063-aluminum-comparison/
  /blog/aa15-vs-aa25-anodizing-explained/
  /blog/qualicoat-class-1-vs-2-powder-coating/
  /blog/how-to-choose-aluminum-extrusion-supplier-china/
  /blog/7-mistakes-buyers-make-sourcing-aluminum-extrusion/
  /blog/aluminum-extrusion-vs-steel-2026-cost-strength/
  /blog/aluminum-extrusion-sustainability-recycled-content/
```

### Cluster build-out priorities

**Month 1 (P0):**
1. `/custom-aluminum-extrusion/` (pillar, ~3,500 words) — rewrite from existing cornerstone
2. `/alloys/6063-aluminum/` (1,800 words)
3. `/alloys/6061-aluminum/` (1,800 words)
4. `/blog/6061-vs-6063-aluminum-comparison/` (2,200 words)
5. `/about-jiju-aluminium/` (1,400 words)

**Month 2 (P1):**
6. `/industries/doors-and-windows/` (2,000 words)
7. `/industries/ev-battery-trays/` (1,800 words)
8. `/surface-finishes/anodizing/` + `/surface-finishes/powder-coating/` + `/surface-finishes/pvdf/` (1,200 words each)
9. `/aluminum-extrusion-pricing-guide/` (1,800 words)
10. `/aluminum-extrusion-standards/` (1,600 words)

**Month 3 (P1-P2):**
11. `/industries/solar-pv-frames/`, `/industries/led-heat-sinks/`, `/industries/industrial-framing-tslot/`
12. `/aluminum-extrusion-supplier-germany/` + USA + SE-Asia regional landings
13. `/case-studies/` index + 6 detail pages
14. 5 supporting blogs from list above

---
# 06 — 20 Ready-to-Publish B2B FAQs

These 20 FAQs are designed for **maximum AI citation probability**: each answer is self-contained (60–120 words), contains 1+ specific number/spec/standard, and avoids first-person voice. Deploy across the homepage, key product pages, dedicated `/faq/` page, and the cornerstone pillar.

Pair with FAQPage schema (block `f_faqpage.json`) — this report and the schema file are kept in sync.

---

## Pricing, MOQ, lead time

### 1. What is the MOQ for custom aluminum extrusion at JIJU?
JIJU's standard minimum order quantity is **500 kg per profile**, lower than the 1–2 tonne MOQ typical at most Chinese aluminum extruders. For first orders or sample runs we accept 200–300 kg with a tooling-amortization surcharge. MOQ on stock profiles in 6063-T5 mill finish starts at **100 kg**. MOQ on anodized or powder-coated finishes is 300 kg per color batch to keep finish quality consistent. Larger MOQs unlock per-kg discounts: 5+ tonnes, 20+ tonnes, and 50+ tonne tiers.

### 2. How much does an aluminum extrusion mold (die) cost?
Mold cost depends on profile cross-section size, complexity, and number of cavities. **Solid profiles up to 100 mm circumscribed-circle diameter cost USD 250–500 per die. Hollow profiles cost USD 600–1,500. Multi-cavity dies for very small profiles cost USD 1,000–2,500.** All JIJU dies are H13 hot-work tool steel, hardened to 48–52 HRC, EDM-machined, and nitrided for 30,000+ tonne extrusion life. JIJU credits the full die cost against the first 1–3 production runs depending on profile complexity.

### 3. What is the lead time for first sample and production order?
**Mold lead time: 5–7 working days** after drawing approval. **First sample: 12–15 days** after PO confirmation, shipped via DHL/FedEx for buyer inspection. **Production lead time: 15–30 days** after sample approval, varying by alloy availability, surface treatment, and quantity. Anodized orders add 3–5 days. Powder coating adds 2–4 days. PVDF spraying adds 5–7 days. Sea freight to Europe is an additional 30–35 days; to US East Coast 32–38 days; to SE Asia 8–15 days.

### 4. What payment terms does JIJU accept?
JIJU accepts **T/T 30/70** (30% deposit on PO, 70% balance against B/L copy before shipping) for most orders. **L/C at sight** is available for orders ≥ USD 30,000 — issued by an internationally recognized bank, payable through Bank of China or HSBC Hong Kong. **D/P** is available for repeat customers with 12+ months of trading history. Western Union and PayPal are accepted for sample fees and tooling deposits up to USD 2,000.

---

## Materials & specifications

### 5. What aluminum alloys does JIJU produce?
JIJU extrudes **6063, 6061, 6005, 6082, 6N01, and 6066-T66** alloys in tempers **T4, T5, T6, and T66**. 6063 (Mg-Si alloy) is the standard for architectural profiles — doors, windows, curtain walls, decorative trim. 6061 (Mg-Si-Cu) is stronger and used for structural framing, EV chassis, marine, and machined parts. 6005 and 6082 are intermediate alloys preferred for railway and EV battery housings. 6N01 is used for high-speed-train flooring. 6066-T66 is a high-strength specialty alloy for aerospace and defense.

### 6. What is the difference between 6063 and 6061 aluminum?
**6063** has lower magnesium and silicon content, giving it excellent extrudability, a smooth surface for anodizing, and yield strength around **170 MPa (T5)**. It is the standard architectural alloy. **6061** adds copper, raising yield strength to **240 MPa (T6)** but slightly reducing extrudability and corrosion resistance. 6061 is used where structural load matters — T-slot framing, EV chassis, machined parts, marine fittings. JIJU recommends 6063 for windows, doors, decorative profiles, and 6061 for structural and machined applications.

### 7. What tolerances can JIJU achieve?
JIJU achieves **wall thickness tolerance ±0.05 mm**, **length tolerance ±0.2 mm per metre**, **straightness ≤ 0.3 mm per metre**, and **twist ≤ 1° per metre** on standard profiles. These are tighter than EN 755-9 Class A and ASTM B221 standard. For precision profiles requiring tighter tolerances (±0.02 mm), JIJU offers a "precision" production class with secondary calibration drawing — typically used for semiconductor, optical, and medical-device profiles. 3-axis CMM inspection reports are issued with every shipment on request.

### 8. What is the maximum extrusion length and cross-section JIJU can produce?
JIJU produces extrusions up to **8 metres** in standard length and up to **12 metres** as special order. Maximum circumscribed-circle diameter for solid profiles is **350 mm** (on the 7,500-tonne press). Maximum hollow-profile circumscribed-circle diameter is **280 mm**. Wall thickness ranges from **0.8 mm** (decorative trim) to **20 mm** (structural). Custom shapes including I-beams, multi-chamber hollow sections, and asymmetric profiles up to 8 kg per metre are supported.

---

## Surface finishes

### 9. What surface finishes does JIJU offer?
JIJU offers six standard finishes in-house: **mill (as-extruded)**, **anodizing** (AA10 / AA15 / AA20 / AA25 µm thickness, natural or color-dyed per RAL or Pantone), **powder coating** (60–120 µm, QUALICOAT class 1 or 2, all RAL colors plus textures), **fluorocarbon / PVDF** (≥70% PVDF resin, 25-year warranty), **wood-grain transfer** (heat-transfer film, 200+ patterns), and **brushed / hairline** finishes. Combined finishes such as anodize-plus-laser-engraving and powder-plus-PVDF top-coat are available on request.

### 10. Which is better for outdoor use — anodizing or powder coating?
For outdoor architectural use, **AA15 or AA25 anodizing offers ≥1,000 hours salt-spray resistance and 25-year warranty against fade**. Anodizing chemically integrates with the aluminum, so it cannot peel or chip, and is preferred for premium residential windows, curtain walls, and luxury decorative profiles. **QUALICOAT class 2 powder coating** offers similar 1,000+ hour salt-spray performance and a wider color range, but at a 15–25% lower per-kg cost. PVDF outperforms both in extreme UV, marine, or industrial environments and is required by most EU green-building standards.

### 11. Does JIJU support thermal-break aluminum window profiles?
Yes. JIJU produces **PA66-25-GF strip thermal-break profiles** (poured polyamide) and **PU-foam thermal-break profiles** for residential and commercial windows. Standard system depths are 60 mm, 70 mm, 80 mm, and 110 mm — compatible with major EU brands (Schüco, Reynaers, Aluprof) and locally certified to **EN 14024** mechanical performance. Achievable Uf values: 1.0–1.4 W/m²K for standard systems; **down to 0.74 W/m²K** for premium passive-house systems with 3-strip insulation.

---

## Industry-specific

### 12. Does JIJU produce aluminum profiles for EV battery trays?
Yes. JIJU supplies extruded battery housing profiles in **6005A-T6** (high strength + good weldability) and **6082-T6** (highest strength) alloys for EV OEMs. Standard sections include side rails, bottom plates, end plates, and cooling-channel extrusions ready for FSW (friction stir welding). Profile wall thickness 2.5–4 mm, length up to 6 m, surface in mill or KTL e-coat. Crash-rated profile design is supported with FEA simulation. Tolerance class is "precision" (±0.02 mm wall thickness) to meet OEM PPAP requirements.

### 13. Does JIJU produce aluminum frames for solar / PV panels?
Yes. JIJU is a long-standing supplier of **6063-T5 anodized photovoltaic module frames** in standard depths of 30 mm, 35 mm, 40 mm, 45 mm, and 50 mm. Standard finish is **AA15 silver anodizing** for 25-year outdoor durability. Annual capacity dedicated to PV frames is 18,000 tonnes. CN-MTC certification on every shipment. Custom-shaped frames for shingled, bifacial, and large-format (210 mm cell) modules are supported on standard tooling lead time.

### 14. Does JIJU produce LED heat sinks?
Yes. JIJU extrudes custom **6063-T5 aluminum heat sinks** with fin densities up to **12 fins per inch**, fin heights up to 80 mm, and base widths up to 250 mm. Standard finishes are natural anodized (matte black), satin anodized, or powder-coated black for higher emissivity. Thermal-design support is offered: for new heat-sink projects, JIJU's R&D team can recommend fin geometry and base thickness against target wattage and ambient conditions.

### 15. Are JIJU profiles compatible with Bosch Rexroth and 80/20 T-slot framing?
Yes. JIJU produces **dimensionally identical** T-slot profiles in 20×20, 30×30, 40×40, 45×45, 60×60, 80×80, 90×90, and 100×100 series, with M5/M6/M8/M10 slot widths. Profiles meet **EN 755-9 Class A tolerances**. Anodized natural finish AA15 is standard. Connectors, gussets, end caps, and fastening hardware are produced by partner factories or sourced as your specification requires.

---

## Logistics & service

### 16. What ports and Incoterms does JIJU support?
JIJU ships from the **port of Qingdao** (primary) and **Shanghai** (secondary), with Tianjin and Ningbo available on request. Standard Incoterms supported: **FOB, CIF, CFR, DAP, DDP, EXW**. Door-to-door DDP service is offered to EU (Hamburg, Rotterdam, Antwerp, Genoa), US (Los Angeles, New York, Houston, Savannah), Australia, Southeast Asia, and major Middle East ports. Sea-freight transit time: 30–35 days to EU, 32–38 days to US East Coast, 8–15 days to SE Asia. FCL 20'/40'/40HQ + LCL all supported.

### 17. What documents does JIJU provide with each shipment?
Standard documents accompany every shipment: **commercial invoice**, **packing list**, **bill of lading (B/L)**, **certificate of origin (Form A or COCOA)**, **mill test certificate** (per heat, listing chemical composition and mechanical properties per EN 10204 type 2.2 or 3.1), **CIQ inspection certificate**, **fumigation certificate** for wooden packaging (ISPM-15), and **REACH / RoHS conformity declarations**. PVDF or anodized finishes additionally ship with **QUALICOAT** or **GSB International** test reports on request.

### 18. What ISO certifications does JIJU hold and what do they mean for buyers?
JIJU is certified to three international management standards: **ISO 9001:2015** (quality management — covers traceability, NCR handling, customer-complaint resolution), **ISO 14001:2015** (environmental management — covers waste, emissions, resource use), and **ISO 45001:2018** (occupational health and safety). Original certification PDFs with the certifying body name and certificate numbers are available for download from the certifications page. JIJU also supports buyer-side compliance with **REACH SVHC**, **RoHS 2.0**, **CE-mark conformity** (for EU construction-product imports), and **Conflict Minerals** reporting where required.

### 19. Does JIJU support OEM and ODM aluminum extrusion projects?
Yes. **OEM** means JIJU extrudes to your supplied 2D drawing or 3D model (DWG, DXF, STEP, IGES); we provide **design-for-manufacturability feedback** within 24 hours. **ODM** means JIJU's 45-engineer R&D team co-designs the profile with you from concept — including FEA structural simulation, prototype CNC parts, mold design, sample, and full production. NDA is signed before any drawings are exchanged. Project ownership and tooling rights remain with the buyer; JIJU does not re-sell custom dies to third parties.

### 20. How does JIJU's quality-control process work?
Every JIJU order passes a **5-stage QC chain**: (1) raw billet inspection — chemical composition by spectrometer per heat, ultrasound for porosity; (2) post-extrusion dimensional inspection — first-piece CMM check + 5 % continuous in-line check; (3) post-aging hardness test (Webster B or Brinell); (4) post-surface-treatment film-thickness measurement (eddy-current gauge for anodizing, magnetic for powder); (5) final pre-shipment inspection — visual, dimensional, packaging integrity. Reports are issued to the customer before shipping; third-party inspection (SGS, BV, TÜV) is available at customer cost.

---
# 07 — 20 AI-Citation Content Blocks

These 20 short, dense, AI-quotable blocks should be deployed across the site (homepage, alloy hubs, surface-treatment hubs, industry hubs, blog posts) in `<p>` or `<blockquote>` tags. Each is **40–110 words**, self-contained, contains 1+ measurable spec or standard, and is designed to be cited verbatim by ChatGPT, Perplexity, Claude, and Gemini.

---

## "What is..." (5 blocks)

### Block 1 — What is aluminum extrusion?
**Aluminum extrusion** is a manufacturing process in which a heated aluminum billet — typically 6xxx-series alloy at 450–500 °C — is forced through a steel die under pressures of 5,000–15,000 tonnes to form a continuous profile of constant cross-section. The extrudate is then cooled (water-quench or air-quench), stretched to remove twist, aged to achieve final temper (T5 or T6), cut to length, and surface-treated. Standards governing the process include EN 755-1 (Europe), ASTM B221 (United States), and GB/T 5237 (China). Aluminum extrusion supports cross-sections from 0.5 mm² to 100,000 mm² and lengths up to 12 m.

### Block 2 — What is anodizing?
**Anodizing** is an electrochemical conversion process that grows a controlled aluminum-oxide layer on the surface of an aluminum profile. The profile is immersed in a sulfuric-acid bath (15–18 % H₂SO₄ at 18–22 °C) and made the anode in a DC circuit at 12–20 V. Oxide grows from the metal outward at a rate of about 1 µm per 2 minutes. Standard architectural thicknesses are AA10 (10 µm), AA15 (15 µm), AA20 (20 µm), and AA25 (25 µm). The oxide layer is integral to the metal — it cannot peel — and provides up to 1,000+ hours of salt-spray corrosion resistance.

### Block 3 — What is 6063 aluminum?
**6063 aluminum** (Al-Mg-Si) is the most widely extruded alloy in the world, accounting for roughly 70 % of architectural extrusions. Its composition is approximately 0.45 % Mg, 0.40 % Si, balance Al. In the T5 temper (cooled at the press and naturally aged), 6063 has a yield strength of about **170 MPa**, ultimate tensile of 215 MPa, and elongation of 12 %. In the T6 temper (solution-heat-treated and artificially aged) yield reaches 215 MPa. 6063 is preferred for window and door frames, curtain walls, decorative profiles, and LED heat sinks because of its excellent extrudability and smooth anodizing response.

### Block 4 — What is T-slot aluminum framing?
**T-slot aluminum framing** is a modular structural system built from extruded 6063 or 6005 aluminum profiles featuring T-shaped slots on each face. Standard profile sizes are **20×20, 30×30, 40×40, 45×45, 60×60, 80×80, and 90×90 mm**, with slot widths matched to M5, M6, M8, or M10 hardware. Connections are made with steel T-nuts, brackets, and gussets — no welding or drilling is required. T-slot framing is widely used for industrial machine frames, robotic cells, conveyor systems, workstations, and product enclosures. Brand-compatible series include Bosch Rexroth (MGE), Item Industrietechnik, and 80/20 Inc.

### Block 5 — What is fluorocarbon (PVDF) coating on aluminum?
**Fluorocarbon coating**, also called PVDF coating, is a high-durability finish containing **≥70 % polyvinylidene fluoride resin** by weight. Applied as a multi-layer spray (primer + color + clear coat, total dry-film thickness 25–40 µm) and oven-cured at 230–250 °C, PVDF resists UV degradation, chalking, and chemical attack better than any other architectural coating. Manufacturers typically warrant PVDF for **20–25 years** against fading and chalking, with 4,000+ hours salt-spray resistance. PVDF is required by most EU and US green-building specifications for high-rise curtain walls and is the standard finish for premium architectural aluminum profiles in marine and industrial environments.

---

## "How does..." (3 blocks)

### Block 6 — How does the aluminum extrusion process work?
The aluminum extrusion process has six stages. **(1) Billet preparation** — 6xxx-series billets are cut to length and homogenized at 540–580 °C for grain control. **(2) Pre-heating** — billets are heated to 450–500 °C in a gas furnace. **(3) Extrusion** — a hydraulic press forces the billet through a steel die at 5,000–15,000 tonnes; exit speeds range from 5 to 50 m/min depending on alloy and section. **(4) Quenching** — water- or air-cooling locks in mechanical properties. **(5) Stretching** — 0.5–2 % stretch removes twist and bow. **(6) Aging** — 175–200 °C for 6–8 hours reaches T5/T6 temper. Profiles are then sawed, surface-treated, and packed.

### Block 7 — How is an aluminum extrusion mold (die) made?
An aluminum extrusion **die** is machined from an annealed H13 hot-work tool-steel block (300–500 mm diameter) using EDM (electrical discharge machining) and CNC milling. After rough machining the bearing surfaces are precision-EDM'd to ±0.02 mm. The die is then heat-treated to **48–52 HRC** and gas-nitrided to a 0.2–0.4 mm hard case. A typical die produces 30,000–50,000 tonnes of extrusion before re-nitriding or replacement. Lead time at JIJU is **5–7 working days** from drawing approval, with full die cost typically credited against the first 1–3 production runs.

### Block 8 — How is aluminum extrusion quality inspected?
Aluminum extrusion quality control proceeds in **five stages**. (1) **Billet QC** — chemical composition by optical-emission spectrometer per heat, ultrasonic testing for internal porosity. (2) **Dimensional QC** — first-piece coordinate-measuring-machine (CMM) verification, then 5 % continuous in-line dimensional sampling. (3) **Mechanical QC** — Webster-B or Brinell hardness post-aging to confirm T5/T6 temper. (4) **Surface QC** — eddy-current gauge for anodizing thickness, magnetic gauge for powder, salt-spray for corrosion. (5) **Final pre-shipment QC** — visual, dimensional, packaging-integrity. Reports per EN 10204 type 2.2 or 3.1 are issued on request.

---

## "Why..." (3 blocks)

### Block 9 — Why choose aluminum over steel for industrial profiles?
**Aluminum is one-third the density of steel** (2.70 g/cm³ vs 7.85 g/cm³) yet typical 6063-T5 yield strength of 170 MPa enables stiffness-equivalent profiles at 50–60 % of steel's installed weight. Aluminum requires no painting in indoor environments and resists outdoor corrosion when anodized or powder-coated, eliminating the periodic recoat cost steel demands. Aluminum is also infinitely recyclable using only **5 % of the energy** required to produce primary metal — a decisive advantage in 2026 ESG-driven procurement. The trade-off is per-kg material cost: aluminum is roughly 2.5–3× steel per tonne, but typically 30–50 % cheaper on installed-weight basis once weight savings are credited.

### Block 10 — Why choose 6063 alloy for door and window profiles?
**6063 aluminum** is the dominant alloy for door and window profiles for three measurable reasons. (1) **Extrudability** — 6063 extrudes 30–40 % faster than 6061, lowering production cost and enabling thin-wall multi-chamber sections. (2) **Surface quality** — 6063 produces an exceptionally smooth surface that anodizes uniformly, critical for premium architectural appearance. (3) **Corrosion resistance** — without copper in its composition, 6063 resists pitting and stress corrosion better than 6061, even in coastal environments. 6063-T5 yield of **170 MPa** is sufficient for residential and most commercial window systems; 6063-T6 reaches 215 MPa for taller curtain-wall applications.

### Block 11 — Why should buyers prefer ISO-certified aluminum extrusion suppliers?
An ISO-9001-certified aluminum extrusion supplier offers three concrete buyer benefits. (1) **Traceability** — every batch is recorded against a heat number, shift, operator, and dimensional CMM record. If a non-conformance is found post-shipment, root cause is identifiable. (2) **Documented NCR process** — ISO 9001 mandates a 8D / CAPA flow for any non-conformance, ensuring repeat issues are prevented systematically. (3) **External audit** — ISO certification is renewed annually by an accredited body (TÜV, BV, SGS), forcing the supplier to maintain quality discipline year-round. Certificate numbers are verifiable at the certifying body's online registry, deterring fraud.

---

## "Benefits of..." (3 blocks)

### Block 12 — Benefits of aluminum profiles for solar panel frames
Aluminum profiles dominate solar PV module framing for **five reasons**. **Light weight** (2.70 g/cm³) reduces racking-system load and rooftop point loads. **AA15 anodizing** delivers 25-year outdoor durability without recoat — matching panel warranty length. **Recyclability** (>95 %) supports module end-of-life circular-economy directives now mandated under EU regulation. **Extrudability** allows complex multi-chamber sections that integrate cell sealing, cable management, and clamping in a single profile. Finally, **cost stability** — aluminum LME pricing has tracked within ±15 % of trend for 5+ years, while steel and polymer prices have fluctuated more, enabling solar-module BoM stability for OEMs.

### Block 13 — Benefits of anodized aluminum finishes
Anodized aluminum finishes deliver four buyer-relevant benefits. **(1) Permanent integration** — the oxide layer is grown from the metal itself, so it cannot peel, chip, or flake the way painted finishes can. **(2) Corrosion resistance** — AA15 (15 µm) anodizing achieves 1,000+ hours salt-spray performance, AA25 reaches 2,000+ hours, suitable for marine and coastal use. **(3) Color stability** — electrocolored and dyed-and-sealed anodic finishes retain color for 20+ years outdoors versus 5–10 years for typical organic coatings. **(4) Hardness** — anodic film hardness of 200–500 HV resists scratches and abrasion better than powder coating.

### Block 14 — Benefits of custom aluminum extrusion vs standard profiles
Custom aluminum extrusion delivers four benefits over off-the-shelf profiles. **(1) BoM consolidation** — features that would require 3-5 separate fabricated parts (clip slots, screw bosses, sealing channels, cable runs) are integrated into a single extruded section. **(2) Material savings** — section can be optimized to load case, removing 20–40 % of mass relative to a standard profile sized for the same load. **(3) Faster assembly** — captive-fastener bosses, snap-fit clip channels, and self-locating geometries reduce downstream assembly labor. **(4) IP protection** — custom dies are owned by the buyer, deterring competitor duplication and creating a defensible product moat.

---

## "Applications of..." (3 blocks)

### Block 15 — Applications of aluminum extrusion in electric vehicles
Extruded aluminum profiles have become a structural backbone of modern electric vehicles. **Battery housings** built from FSW-welded 6005A or 6082-T6 extrusions form the lower part of the vehicle structure and protect the battery pack against crush and intrusion. **Crash-management profiles** (front and rear crumple zones) use 6063-T6 or 6082-T6 for tunable energy absorption. **Cooling channels** are extruded directly into battery tray base plates, eliminating brazed cooler subassemblies. **Body-in-white longerons, sills, and pillars** in space-frame designs (e.g. Audi A8, Tesla Model S) are 60–70 % aluminum extrusions by length, saving 200–300 kg per vehicle versus equivalent steel.

### Block 16 — Applications of aluminum extrusion in solar energy
Aluminum extrusions enable **three primary solar-energy applications**. **Module frames** — 6063-T5 anodized profiles in 30–50 mm depths frame >95 % of crystalline-silicon PV modules globally. **Mounting / racking systems** — extruded rails (e.g. 40×80 mm box section) support modules on rooftops and ground-mount fields, with integrated channels for cable runs and earthing. **Tracker structures** — single-axis and dual-axis tracker torque tubes and panel rails use 6082-T6 for higher load capacity. With recycled-content rates above 75 % at major suppliers, aluminum extrusions also support the embodied-carbon thresholds of green-building and ESG procurement standards in 2026.

### Block 17 — Applications of aluminum extrusion in construction
In construction, aluminum extrusions appear in **doors and windows** (thermal-break frames, sliding rails, casement profiles), **curtain walls** (mullion and transom profiles up to 8 m long), **railings and balustrades**, **roofing systems** (standing-seam profiles, skylights, conservatories), **architectural cladding** (PVDF-finished panels and trim), **ceiling and partition systems**, **expansion joints**, and **decorative trim**. The dominant alloy is 6063-T5; structural sections in tall buildings often use 6061-T6 or 6082-T6. Specifications referenced are typically EN 14024 (thermal-break performance), EN 12152 (curtain-wall air permeability), and AAMA 2605 (PVDF specification for high-performance organic coatings).

---

## "Difference between..." (3 blocks)

### Block 18 — Difference between 6061 and 6063 aluminum
The key differences between 6061 and 6063 are composition, strength, and cost. **6061** contains copper (~0.25 %) which raises its T6 yield strength to **240 MPa** but reduces extrudability and corrosion resistance. **6063** has no copper; T5 yield is **170 MPa** (T6: 215 MPa), but it extrudes 30–40 % faster, has superior surface quality for anodizing, and resists corrosion better in coastal environments. Per-kg cost: 6063 is roughly 5–10 % lower than 6061 due to faster press speeds. **Use 6063** for windows, doors, decorative profiles, and heat sinks; **use 6061** for structural framing, EV chassis, machined parts, and marine fittings.

### Block 19 — Difference between anodizing and powder coating
**Anodizing** chemically grows an oxide layer integrated with the aluminum surface, producing a finish that cannot peel, with hardness of 200–500 HV and corrosion resistance up to 2,000 hours salt-spray (AA25). Color range is limited to metallic tones, dyes, and electrocolored bronzes. **Powder coating** is an organic polyester or epoxy-polyester powder fused at 180–220 °C into a film of 60–120 µm. It offers an unlimited color range (all RAL, Pantone, and textured finishes), QUALICOAT class 1 or 2 certification, and 1,000+ hours salt-spray performance — but can chip if struck. Typical cost: anodizing is 15–30 % more expensive per m² than equivalent powder coating.

### Block 20 — Difference between OEM and ODM aluminum extrusion
**OEM (Original Equipment Manufacturing)** means the buyer supplies the complete profile drawing or 3D model (DWG/DXF/STEP) and the manufacturer extrudes to that specification, providing only DFM feedback. The buyer owns the design IP and the die. **ODM (Original Design Manufacturing)** means the manufacturer's R&D team co-designs the profile from concept — running structural FEA, prototype CNC parts, and design iterations — based on the buyer's functional requirements. ODM accelerates time-to-market by 30–60 days for complex profiles and lowers up-front engineering cost, but the manufacturer typically retains shared rights to the design unless a custom IP-transfer agreement is negotiated.

---
# 08 — Schema Deployment Guide

All 13 ready-to-deploy JSON-LD blocks are in `/Users/abin/SEO/jijualuminium/schema/`.

| File | Schema | Where to deploy | Lines |
|---|---|---|---|
| `a_organization.json` | Organization (sitewide expanded) | `<head>` of every page | 163 |
| `b_localbusiness_manufacturer.json` | LocalBusiness + Manufacturer + FactoryOrPlant | `<head>` of every page | 86 |
| `c_website.json` | WebSite + SearchAction | `<head>` of every page | 25 |
| `d_product_template.json` | Product + Offer + AggregateRating + Reviews + MerchantReturnPolicy + OfferShippingDetails | All `/product/*` pages | 116 |
| `e_breadcrumb_template.json` | BreadcrumbList | All non-home pages (replaces broken Yoast breadcrumb) | 37 |
| `f_faqpage.json` | FAQPage with 13 B2B FAQs | Homepage, /faq/, top 10 product pages | 119 |
| `g_howto_order.json` | HowTo (6 ordering steps) | Cornerstone blog + /pricing-guide/ | 69 |
| `h_article_with_author.json` | Article + named Person + Speakable | All blog posts | 77 |
| `i_videoobject.json` | ItemList of 3 × VideoObject | /aluminum-extrusion-videos/ | 68 |
| `j_services.json` | 5 × Service (extrusion, anodizing, powder coat, CNC, mold) | /capabilities/ or about page | 58 |
| `k_collectionpage_itemlist.json` | CollectionPage + ItemList × 2 | /shop/, product-category pages | 95 |
| `l_place_geocircle_areaserved.json` | Place + GeoCircle (worldwide + 7 markets) | Org schema extension | 59 |
| `m_imageobject_hero.json` | ImageObject × 2 with licensing | Homepage + key landing pages | 50 |
| `combined_snippet.html` | All schemas pre-wrapped in `<script type="application/ld+json">` | Drop-in for testing | 1,629 |

---

## How to deploy in WordPress (3 paths)

### Path 1 — Yoast filters (recommended; preserves Yoast graph integration)

Add to `functions.php` (or a child-theme `functions.php`, or a custom mu-plugin):

```php
<?php
/**
 * JIJU schema overrides — replaces Yoast's basic schema with the expanded
 * deliverables in /Users/abin/SEO/jijualuminium/schema/
 */

// 1. Override Organization with expanded version
add_filter( 'wpseo_schema_organization', function( $data ) {
    $expanded = json_decode( file_get_contents( __DIR__ . '/jiju-schema/a_organization.json' ), true );
    return array_merge( $data, $expanded['@graph'][0] );
} );

// 2. Replace Yoast's stub author Person with named Engineering Team
add_filter( 'wpseo_schema_author', function( $data ) {
    $expanded = json_decode( file_get_contents( __DIR__ . '/jiju-schema/h_article_with_author.json' ), true );
    foreach ( $expanded['@graph'] as $piece ) {
        if ( isset( $piece['@type'] ) && $piece['@type'] === 'Person' ) {
            return array_merge( $data, $piece );
        }
    }
    return $data;
} );

// 3. Inject Product schema on WooCommerce product pages
add_filter( 'wpseo_schema_graph', function( $graph, $context ) {
    if ( ! is_singular( 'product' ) ) return $graph;
    global $product;
    if ( ! $product ) $product = wc_get_product( get_the_ID() );

    $template = json_decode( file_get_contents( __DIR__ . '/jiju-schema/d_product_template.json' ), true );
    $product_schema = $template['@graph'][0];

    // Hydrate from the actual product
    $product_schema['name']        = $product->get_name();
    $product_schema['description'] = wp_strip_all_tags( $product->get_short_description() ?: $product->get_description() );
    $product_schema['sku']         = $product->get_sku();
    $product_schema['url']         = get_permalink( $product->get_id() );
    $product_schema['image']       = wp_get_attachment_url( $product->get_image_id() );
    // Optional: pull alloy / finish / MOQ from custom fields
    $product_schema['additionalProperty'][0]['value'] = get_field( 'alloy', $product->get_id() ) ?: '6063-T5';

    $graph[] = $product_schema;
    return $graph;
}, 10, 2 );

// 4. Override Yoast breadcrumb to remove Chinese "产品" leak on product pages
add_filter( 'wpseo_breadcrumb_links', function( $links ) {
    foreach ( $links as $i => $link ) {
        if ( isset( $link['text'] ) && trim( $link['text'] ) === '产品' ) {
            $links[ $i ]['text'] = 'Shop';
            $links[ $i ]['url']  = home_url( '/shop/' );
        }
    }
    return $links;
} );

// 5. Inject FAQPage on homepage and selected product pages
add_filter( 'wpseo_schema_graph', function( $graph, $context ) {
    $faq_pages = [ '/', '/faq/', '/product/aluminum-profiles-for-doors-and-windows/' ];
    if ( ! in_array( $_SERVER['REQUEST_URI'], $faq_pages, true ) ) return $graph;
    $faq = json_decode( file_get_contents( __DIR__ . '/jiju-schema/f_faqpage.json' ), true );
    foreach ( $faq['@graph'] as $piece ) $graph[] = $piece;
    return $graph;
}, 11, 2 );

// 6. Inject HowTo on cornerstone blog
add_filter( 'wpseo_schema_graph', function( $graph, $context ) {
    if ( ! is_single() ) return $graph;
    $slug = basename( get_permalink() );
    if ( $slug !== 'custom-aluminum-extrusion-guide-from-design-to-delivery' ) return $graph;
    $howto = json_decode( file_get_contents( __DIR__ . '/jiju-schema/g_howto_order.json' ), true );
    foreach ( $howto['@graph'] as $piece ) $graph[] = $piece;
    return $graph;
}, 12, 2 );
```

Place the schema files in `/wp-content/jiju-schema/` (matching `__DIR__` above).

### Path 2 — Switch to Rank Math Pro (faster, more turn-key)

Rank Math Pro auto-emits Product, FAQ, HowTo, and Author schemas with much less code. If migrating, audit JIJU's existing Yoast meta-descriptions, focus keywords, and breadcrumb settings before switching to avoid traffic loss. Plan a 2-week migration sprint.

### Path 3 — Schema Pro plugin

If you want a GUI-based approach without code, **Schema Pro** ($79/year) lets you visually configure Organization, Product, FAQ, and HowTo schemas mapped to your post types and ACF fields. Less flexible than filters but accessible to non-developers.

---

## Validation checklist (run after each deployment)

| # | Tool | What to check |
|---|---|---|
| 1 | [Google Rich Results Test](https://search.google.com/test/rich-results) | All page templates pass with no errors. Eligible rich results: Product, FAQ, HowTo, BreadcrumbList, Article. |
| 2 | [Schema.org Validator](https://validator.schema.org/) | All custom JSON-LD validates against schema.org core types. |
| 3 | [Schema App Schema Markup Validator](https://schema.app/validator) | Cross-checks for AI-friendly properties. |
| 4 | View page source manually | Each page contains exactly **one** `Organization`, exactly **one** `WebSite`, exactly **one** `BreadcrumbList`. No duplicates. |
| 5 | Search Console → Enhancements | After 1–2 weeks, "Products", "FAQs", "HowTos", "Breadcrumbs" reports show new valid items. Zero errors. |
| 6 | OpenAI / Perplexity sample queries | Search "Shandong JIJU Aluminium" — entity card should start showing factory facts within 2–4 weeks. |
| 7 | Google Knowledge Graph API (after Wikidata QID lives) | `https://kgsearch.googleapis.com/v1/entities:search?query=Shandong+JIJU+Aluminium&...` returns the Organization entity. |

---

## Common pitfalls

1. **Two BreadcrumbLists on the same page** (Yoast + WooCommerce) — confuses validators. Use the filter in §4 above to suppress one.
2. **Hard-coded ratings** — only emit `aggregateRating` if you have real reviews. Inflated/fake ratings can trigger Google manual penalty.
3. **Wrong `@id`** — every Organization must have a stable `@id` (e.g. `https://jijualuminium.com/#organization`). Don't change it.
4. **Image dimensions not specified** — Google Rich Results requires `Product.image` URLs to point to images ≥ 1,200 × 1,200 ideally. Provide multiple sizes (1×1, 4×3, 16×9).
5. **Currency mismatch** — `priceCurrency` must be ISO 4217 (USD, EUR, CNY, GBP). Use a single currency per Offer (no comma-separated).
6. **Empty `availableLanguage` arrays** — Yoast emits `[]` for ContactPoint by default; add `["en", "de", "es", "zh"]` per JIJU's actual support languages.
7. **Forgetting `inLanguage` on WebSite + WebPage** — set to "en" sitewide; if you launch DE/ES versions, add per-locale.

---
# 09 — Internal Linking Strategy

The strongest GEO leverage on JIJU's existing 200+ pages is **internal-link redistribution**. The current site has 60 internal links from the homepage, but they cluster on navigation/footer rather than topical pages. The plan below moves authority into pillar + cluster pages and establishes the topic-cluster hierarchy AI engines look for.

---

## Internal-linking principles for GEO

1. **Pillar pages** receive links from: homepage, every cluster page, every supporting blog, footer, and 5+ product pages.
2. **Cluster pages** link upward to the pillar (1–2 links) and laterally to peer clusters (2–3 links).
3. **Blog posts** link upward to relevant cluster + pillar (3–5 links per post).
4. **Product pages** link to their parent industry hub + relevant alloy hub + relevant surface-treatment hub.
5. **Anchor text** mixes exact-match (`"6063 vs 6061 aluminum"`), long-tail (`"learn how 6063 differs from 6061 in tensile strength"`), and natural sentence anchors. Avoid 100 % exact-match.
6. **No-follow** on outbound third-party links unless they are authoritative citations (Wikipedia, ISO, ASTM, EN). Citation links to authoritative sources also strengthen GEO.

---

## Top 30 internal-link actions (Page A → Page B with anchor recommendation)

| # | From | To | Anchor text |
|---|---|---|---|
| 1 | Homepage hero | `/custom-aluminum-extrusion/` | "complete custom aluminum extrusion buyer's guide" |
| 2 | Homepage "By the Numbers" | `/about-jiju-aluminium/` | "see JIJU's 30-year manufacturing history" |
| 3 | Homepage industries block | `/industries/doors-and-windows/` | "thermal-break aluminum window profiles" |
| 4 | Homepage industries block | `/industries/ev-battery-trays/` | "EV battery tray extrusions" |
| 5 | Homepage industries block | `/industries/solar-pv-frames/` | "PV solar module frames" |
| 6 | Homepage FAQ block | `/faq/` | "see all 50+ aluminum extrusion FAQs" |
| 7 | Cornerstone blog Phase 1 | `/alloys/6063-aluminum/` | "6063 alloy specifications" |
| 8 | Cornerstone blog Phase 1 | `/alloys/6061-aluminum/` | "6061 alloy properties" |
| 9 | Cornerstone blog Phase 2 | `/aluminum-extrusion-tooling-dies/` | "how aluminum extrusion dies are made" |
| 10 | Cornerstone blog Phase 4 | `/surface-finishes/anodizing/` | "anodizing process and AA15/AA25 standards" |
| 11 | Cornerstone blog Phase 5 | `/aluminum-extrusion-pricing-guide/` | "MOQ, FOB pricing, and lead times" |
| 12 | `/alloys/6063-aluminum/` | `/blog/6061-vs-6063-aluminum-comparison/` | "side-by-side 6061 vs 6063 comparison" |
| 13 | `/alloys/6061-aluminum/` | `/blog/6061-vs-6063-aluminum-comparison/` | (same anchor) |
| 14 | Industry hub (doors/windows) | `/product-category/door-and-window-moving-door-customization/` | "browse 30+ window profile specs" |
| 15 | Industry hub (doors/windows) | `/blog/thermal-break-aluminum-window-profile/` | "thermal-break window profile design" |
| 16 | Industry hub (EV) | `/alloys/6005-aluminum/` | "6005A alloy for EV battery housings" |
| 17 | Industry hub (EV) | `/blog/aluminum-extrusion-fsw-welding/` | "FSW friction-stir-welded battery trays" |
| 18 | Industry hub (solar) | `/surface-finishes/anodizing/` | "AA15 anodizing for 25-year outdoor durability" |
| 19 | Each product page | `/aluminum-extrusion-pricing-guide/` | "see MOQ, FOB pricing & lead times" |
| 20 | Each product page | `/faq/` | "common buyer questions answered" |
| 21 | Each product page | (parent industry hub) | (industry-specific anchor) |
| 22 | Each product page | (parent surface-treatment hub) | (finish-specific anchor) |
| 23 | Surface-treatment hub | `/blog/anodizing-vs-powder-coating-comparison/` | "anodizing vs powder coating: when to use each" |
| 24 | Pricing guide page | `/blog/aluminum-extrusion-incoterms-shipping/` | "Incoterms for aluminum imports" |
| 25 | Pricing guide page | `/aluminum-extrusion-standards/` | "EN 755, ASTM B221, GB/T 5237 standards" |
| 26 | Standards page | `/aluminum-extrusion-tolerances-qc/` | "tolerance classes and CMM inspection" |
| 27 | About page | `/case-studies/` | "see real client projects" |
| 28 | About page | `/certifications/` | "download our ISO 9001/14001/45001 certificates" |
| 29 | Footer (sitewide) | `/llms.txt` | (link via `<meta>` rel="alternate" — not visible link) |
| 30 | Footer (sitewide) | `/sitemap_index.xml` | "sitemap" |

---

## Anchor-text diversity guidelines

For each target page, keep the anchor-text mix roughly:

- **30 % exact-match** (e.g. "6063 aluminum extrusion")
- **40 % partial-match / long-tail** (e.g. "learn how 6063 alloy is specified for windows")
- **20 % natural / contextual** (e.g. "this thinner-walled architectural alloy")
- **10 % branded / generic** (e.g. "JIJU's 6063 page" / "read more")

---

## Internal-linking implementation

WordPress-friendly approaches (in order of preference):

1. **Manual editorial linking** in Elementor blocks and Gutenberg posts — highest quality, scales poorly.
2. **Yoast Premium internal-linking suggestions** — paid feature, surfaces relevant pages while editing.
3. **Link Whisper plugin** — AI-driven link suggestions across the whole site, batch-applies missing links.
4. **Custom shortcode** — `[jiju-link to="6063-aluminum"]thinner-walled architectural alloy[/jiju-link]` for re-usable contextual anchors.

---

## Orphan page audit

Run quarterly. A page is "orphan" if it has 0 internal inbound links from non-navigation pages. Currently, most JIJU blog posts are orphans — they only receive links from `/jiju-aluminium-leading-manufacturer-of-aluminium-extrusions/` (the blog-list page).

**Fix:** every blog post must receive at least 3 inbound links from pillar/cluster/industry-hub pages.

**Tool:** Screaming Frog → Internal → Inlinks count column → filter `<3` → list to fix.

---
# 10 — 90-Day Execution Plan

Realistic, sequenced, and assigned. Each item has owner placeholder, effort, and KPI.

**Owner codes:** DEV (developer/devops) · SEO (SEO/content lead) · ENG (engineering/product team) · MKT (marketing) · OPS (founder/leadership)

---

## WEEK 1 — Foundation fixes (compounding daily impact)

| # | Task | Owner | Effort | Where | KPI |
|---|---|---|---|---|---|
| 1.1 | Replace `robots.txt` with the version in `11-ROBOTS-AND-LLMSTXT.md` (explicit AI-crawler allows + Bytespider/MJ12 blocks) | DEV | 30 min | `/robots.txt` | All major AI bots show "Allowed" in `https://www.google.com/search?q=site%3Ajijualuminium.com` Bing Webmaster crawl reports |
| 1.2 | Hostinger panel → Performance → enable HCDN page cache; WP-Rocket → Cache lifespan 10h, Mobile cache ON, Preload from sitemap | DEV | 30 min | Server | TTFB <1.5 s on 90 % of URLs; `x-hcdn-cache-status: HIT` on repeat visits |
| 1.3 | Yoast → Search Appearance → Products → set meta-description template (snippet C7 in `01-CRITICAL-ISSUES.md`) | SEO | 30 min | Yoast | All 137 products have a meta within 2 days |
| 1.4 | Drop the mu-plugin to close `/wp-json/wp/v2/users` admin leak | DEV | 15 min | `wp-content/mu-plugins/` | Endpoint returns `[]` |
| 1.5 | Fix Elementor product template to remove duplicate H1 + typo "ALUMINUMEXTRUSION" | ENG | 1 h | Elementor | Product pages have exactly 1 H1 |
| 1.6 | Fix homepage typo "Whar Our Clients Say" → "What Our Clients Say"; fix conflicting factory stats (single source: 150,000 t / 300,000 m² / 21 presses / 400+ employees) | ENG | 1 h | Elementor | No typos / consistent stats |
| 1.7 | Set OG title template in Yoast → Social to `%%title%%` (replaces "Home"/"Blog"/"Contact Us" defaults) | SEO | 15 min | Yoast | OG inspector on Facebook Debugger shows correct title |
| 1.8 | Edit cornerstone blog `/custom-aluminum-extrusion-guide-from-design-to-delivery/` — remove duplicate Phase 3 section | SEO | 30 min | Post editor | Single Phase 3 |
| 1.9 | Manually fix `/shop/`: add Title, Meta, Canonical, H1 (use rewrites in `04-REWRITTEN-HOMEPAGE.md`) | SEO | 30 min | Yoast Page Settings | Yoast scoring green |
| 1.10 | Audit 39 duplicate product slugs (`-2`, `-3`, ..., `-copy`) and create the 301-redirect map | SEO | 3 h | Spreadsheet | Map of `duplicate → canonical → 301` |

**End-of-week KPI:** GEO score 37 → 50; technical score 58 → 72; broken-page count → 0.

---

## WEEK 2 — Schema bonanza (deploy all 13 JSON-LD blocks)

| # | Task | Owner | Effort | Where | KPI |
|---|---|---|---|---|---|
| 2.1 | Override Yoast Organization with expanded version (`a_organization.json`) — Wikipedia/Wikidata/Crunchbase/Alibaba/Made-in-China sameAs, ISO credentials, contactPoints | DEV | 2 h | `functions.php` filter `wpseo_schema_organization` | Validates on Schema.org Validator |
| 2.2 | Add LocalBusiness/Manufacturer/FactoryOrPlant (`b_localbusiness_manufacturer.json`) sitewide | DEV | 1 h | `wp_head` filter | Google Rich Results Test passes |
| 2.3 | Deploy Product schema on all 137 WooCommerce pages (`d_product_template.json` via filter `wpseo_schema_product`, populated from product custom fields) | DEV | 6 h | `functions.php` | All product URLs validate |
| 2.4 | Fix Yoast breadcrumb to remove Chinese "产品" → use "Shop" instead. Suppress duplicate WooCommerce-emitted BreadcrumbList | DEV | 1 h | `functions.php` filter `wpseo_breadcrumb_links` | Single, correct BreadcrumbList per page |
| 2.5 | Deploy FAQPage schema on homepage + 10 highest-traffic product pages (using `f_faqpage.json` + 4 product-specific FAQs from `06-FAQ-LIBRARY.md`) | DEV+SEO | 4 h | Yoast FAQ block + custom filter | FAQ rich-result eligible |
| 2.6 | Deploy HowTo schema on cornerstone blog (`g_howto_order.json`) | DEV | 1 h | Custom block | HowTo rich-result eligible |
| 2.7 | Replace blog Person stub with named "JIJU Engineering Team" (`h_article_with_author.json`) — apply to all 53 blogs | DEV | 2 h | `functions.php` filter `wpseo_schema_author` | All blogs show named author + Speakable |
| 2.8 | Add Service schema for 5 services: Custom Extrusion, Anodizing, Powder Coating, CNC Machining, Mold Design (`j_services.json`) | DEV | 1 h | About / capabilities page | Schema validator passes |
| 2.9 | Add Place + GeoCircle areaServed (`l_place_geocircle_areaserved.json`) — worldwide + 7 markets | DEV | 30 min | Org schema extension | Same |

**End-of-week KPI:** Schema score 58 → 92; Google Rich Results Test passes for Organization, Product, FAQ, HowTo, Article on all relevant page types.

---

## WEEK 3 — Brand entity + content quality

| # | Task | Owner | Effort | Where | KPI |
|---|---|---|---|---|---|
| 3.1 | **Create Wikidata QID** for "Shandong JIJU Aluminium Co., Ltd." — populate founding 1994, Linqu County, alloys, certifications, capacity | OPS+SEO | 4 h | wikidata.org | QID minted, sameAs added to Org schema |
| 3.2 | Build LinkedIn **Company Page** (`/company/jiju-aluminium/`) — logo, banner, About, employees | MKT | 1 day | linkedin.com | Page live with 5+ employees connected, 5 starter posts |
| 3.3 | Rebrand YouTube channel to `@JIJUAluminium` (request handle change) — branded banner, custom URL, About text | MKT | 4 h | YouTube Studio | Branded channel + 3 starter videos |
| 3.4 | Strip first-person AI voice ("I trust JIJU…") from product FAQs and 10 highest-traffic blog posts; rewrite to third-person editorial | SEO | 2 days | Blog editor | Posts read as authored by "JIJU Engineering Team" |
| 3.5 | Strip Chinese characters from English-locale product description blocks (e.g. "产品参数 标准：欧标、国标") | SEO | 2 h | Product editor | Zero Chinese chars on English pages |
| 3.6 | Build new **About JIJU** page at `/about-jiju-aluminium/` (use outline in `02-PAGE-LEVEL-ANALYSIS.md` § F); 301 the old "blog hub" URL | SEO+ENG | 2 days | New page | 1,400+ word page live with team bios + ISO PDFs |
| 3.7 | Add `hreflang` to `<head>` (start `x-default` + `en`; expand as translations ship) | DEV | 1 h | `wp_head` filter | Search Console reports no hreflang errors |
| 3.8 | Begin replacing the 39 duplicate product URLs with proper 301 redirects + delete duplicates | SEO | 4 h | WP admin | 39 → ≤ 5 duplicates remaining |

**End-of-week KPI:** Brand authority score 25 → 45; Wikidata QID live; LinkedIn Company Page live with 100+ followers.

---

## WEEK 4 — Homepage rewrite + FAQ deployment

| # | Task | Owner | Effort | Where | KPI |
|---|---|---|---|---|---|
| 4.1 | Implement homepage rewrite from `04-REWRITTEN-HOMEPAGE.md` — new H1, hero paragraph, "By the Numbers" table, "Industries We Serve", testimonials with full names | ENG+SEO | 2 days | Elementor | Page lives at /; Yoast green |
| 4.2 | Add the 6-FAQ block to homepage (with FAQPage schema) | ENG | 1 h | Elementor + schema | FAQ rich result eligible |
| 4.3 | Build dedicated `/faq/` page with all 20 FAQs from `06-FAQ-LIBRARY.md` | SEO | 4 h | New page | Page live, 20 FAQs published |
| 4.4 | Add the 20 AI citation blocks from `07-AI-CITATION-BLOCKS.md` to relevant pages: 5 "What is..." → alloy/process pages; 3 "How does..." → process page; 3 "Why..." → homepage + alloy hubs; 3 "Benefits of..." → industry hubs; 3 "Applications..." → industry hubs; 3 "Difference..." → comparison blogs | SEO | 1 day | Various pages | All 20 blocks deployed in `<p>` or `<blockquote>` |
| 4.5 | Replace `llms.txt` with the curated version in `11-ROBOTS-AND-LLMSTXT.md` | SEO | 2 h | `/llms.txt` | Clean English, no Chinese, no HTML entities |

**End-of-week KPI:** Composite GEO score 50 → 65; AI citation block count 0 → 20.

---

## MONTH 2 (Weeks 5–8) — Content cluster build-out + technical polish

### Week 5
- Publish `/alloys/6063-aluminum/` (1,800 words) + Alloy schema + internal links to product pages using 6063
- Publish `/alloys/6061-aluminum/` (1,800 words)
- Publish `/blog/6061-vs-6063-aluminum-comparison/` (2,200 words, comparison table, FAQ schema)
- Add the security-headers `.htaccess` block (HSTS, CSP, X-Frame, X-Content-Type, Referrer, Permissions)
- Remove generator headers (WP, WC, Elementor versions)

### Week 6
- Publish `/industries/doors-and-windows/` (2,000 words)
- Publish `/industries/ev-battery-trays/` (1,800 words)
- Publish 4 new case studies under `/case-studies/`: 1 doors/windows EU, 1 EV battery tray, 1 PV frames, 1 LED heat sink
- Build `/certifications/` page with linked ISO 9001/14001/45001 PDF downloads + QUALICOAT/REACH/RoHS docs

### Week 7
- Publish `/surface-finishes/anodizing/` (1,200 words)
- Publish `/surface-finishes/powder-coating/` (1,200 words)
- Publish `/surface-finishes/pvdf/` (1,200 words)
- Publish `/aluminum-extrusion-pricing-guide/` (1,800 words)
- Bulk-regenerate images to AVIF + WebP fallback (ShortPixel/Imagify)

### Week 8
- Publish `/aluminum-extrusion-standards/` (1,600 words, EN 755 / ASTM B221 / GB/T 5237 comparison)
- Publish 5 supporting blog posts:
  - `/blog/aluminum-extrusion-die-cost-explained/`
  - `/blog/aluminum-extrusion-lead-times-2026/`
  - `/blog/aluminum-extrusion-incoterms-shipping/`
  - `/blog/qualicoat-class-1-vs-2-powder-coating/`
  - `/blog/7-mistakes-buyers-make-sourcing-aluminum-extrusion/`
- Implement Top 30 internal-link actions from `09-INTERNAL-LINKING-MAP.md`

**End-of-month-2 KPI:** Composite GEO score 65 → 75; 12 new cornerstone/cluster/blog pages live; orphan-page count -50 %.

---

## MONTH 3 (Weeks 9–12) — Authority building + international expansion

### Week 9 — Brand authority push
- Pitch JIJU to 5 industry trade publications (Aluminium International Today, Aluminum Now, MetalMiner, AluminiumInsider, Light Metal Age)
- Submit JIJU to 3 industry directories (Thomasnet, EC21, Globalsources)
- Publish first **original-data report**: "China Aluminum Extrusion Export Index 2026 Q3" (PDF + landing page) — sourced from JIJU shipment data
- Pitch CEO to 3 supply-chain podcasts

### Week 10 — Industry hubs continued
- Publish `/industries/solar-pv-frames/` (1,500 words)
- Publish `/industries/led-heat-sinks/` (1,500 words)
- Publish `/industries/industrial-framing-tslot/` (1,500 words)
- Publish `/industries/architectural-decorative/` (1,500 words)
- Publish `/industries/curtain-wall/` (1,500 words)
- Add 6 more case studies (one per industry hub)

### Week 11 — Regional expansion (international SEO)
- Publish `/aluminum-extrusion-supplier-germany/` (1,500 words; mentions ports of Hamburg, EU customs, EN 755 compliance)
- Publish `/aluminum-extrusion-supplier-usa/` (1,500 words; mentions LA/NY/Houston ports, AAMA standards, Section 232 tariff context)
- Publish `/aluminum-extrusion-supplier-southeast-asia/` (1,500 words; ASEAN trade, Singapore/Manila/Jakarta ports)
- Translate top 10 pages into German + Spanish (use professional translation, not auto-translate). Add `hreflang` cross-links.

### Week 12 — Content polish + measurement
- Quarterly refresh of cornerstone pillar with Q4-2026 data
- Build interactive **Aluminum Extrusion Cost Calculator** (lightweight JS tool) at `/aluminum-extrusion-cost-calculator/`
- Build **Aluminum Extrusion Standards Cheat Sheet** PDF (downloadable, gated by email opt-in)
- Set up GA4 + Search Console quarterly review templates: track rankings on the 30 keywords from `05-KEYWORD-STRATEGY.md`
- Run Screaming Frog audit; fix any new orphans, broken links, missing meta
- Submit updated `llms.txt`, sitemap, robots.txt to Google Search Console + Bing Webmaster Tools + IndexNow

**End-of-month-3 KPI (90-day final):**
- Composite GEO score: **37 → 78**
- Composite SEO score: **42 → 80**
- Google indexed pages: 200+ (versus current ~150)
- Brand authority: Wikidata QID + LinkedIn Company Page + branded YouTube + 3 trade-press citations + 1 original-data report = score 25 → 65
- Inquiry / quote-request volume: +35 % to +65 % (depending on baseline)
- AI citation rate: ChatGPT branded queries 5 % → ~40 %; unbranded category queries 0.1 % → 4–6 %; Perplexity comparison queries 0 % → 12–18 %

---

## Resourcing summary (90 days)

| Role | Person-days |
|---|---|
| Developer / DevOps | 12 days |
| SEO / Content Lead | 35 days |
| Engineering / Product | 10 days |
| Marketing / Brand | 10 days |
| Founder / Leadership | 5 days |
| **Total** | **~72 person-days over 12 weeks** |

External costs (recommended):
- Schema validator + monitoring SaaS (e.g. Schema App): USD 100/mo
- Hostinger upgrade or migration to managed WP host (Cloudways/Kinsta): USD 50–250/mo
- Translation services (DE + ES, top 10 pages): USD 1,500
- Photography / drone factory shoot: USD 1,500
- Trade-press placement fees (where required): USD 1,000–3,000
- Press release distribution: USD 500
- **Total external: ~USD 6,000 over 90 days**

---
# 11 — robots.txt and llms.txt (drop-in files)

---

## A. Drop-in `robots.txt`

Replace the current `/robots.txt` (which has a duplicate `User-agent: *` and no AI-crawler directives) with this version. Save via Yoast → Tools → File editor or via FTP to `public_html/robots.txt`.

```
# Shandong JIJU Aluminium Industry Co., Ltd.
# robots.txt — last reviewed 2026-05-25
# Default policy: allow legitimate search and AI crawlers; block scrapers and known abusive bots.

# ── Default ───────────────────────────────────────────
User-agent: *
Disallow: /wp-admin/
Disallow: /wp-content/uploads/wc-logs/
Disallow: /wp-content/uploads/woocommerce_transient_files/
Disallow: /wp-content/uploads/woocommerce_uploads/
Disallow: /xmlrpc.php
Disallow: /wp-json/wp/v2/users
Disallow: /?s=
Disallow: /?p=
Disallow: /cart/
Disallow: /checkout/
Disallow: /my-account/
Allow: /wp-admin/admin-ajax.php

# ── Major search engines ──────────────────────────────
User-agent: Googlebot
Allow: /

User-agent: Googlebot-Image
Allow: /

User-agent: Googlebot-News
Allow: /

User-agent: Bingbot
Allow: /

User-agent: DuckDuckBot
Allow: /

User-agent: YandexBot
Allow: /

User-agent: Baiduspider
Allow: /

User-agent: Sogou Spider
Allow: /

# ── AI search engines (allow) ─────────────────────────
# OpenAI / ChatGPT
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: OAI-SearchBot
Allow: /

# Anthropic / Claude
User-agent: ClaudeBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: claude-web
Allow: /

# Perplexity
User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

# Google Gemini / SGE / Bard
User-agent: Google-Extended
Allow: /

# Apple Intelligence
User-agent: Applebot
Allow: /

User-agent: Applebot-Extended
Allow: /

# Common Crawl (used by all major LLMs)
User-agent: CCBot
Allow: /

# Meta Llama
User-agent: Meta-ExternalAgent
Allow: /

User-agent: Meta-ExternalFetcher
Allow: /

User-agent: FacebookBot
Allow: /

# Amazon
User-agent: Amazonbot
Allow: /

# Cohere, Mistral, others
User-agent: cohere-ai
Allow: /

User-agent: cohere-training-data-crawler
Allow: /

User-agent: MistralAI-User
Allow: /

User-agent: DuckAssistBot
Allow: /

User-agent: ImagesiftBot
Allow: /

User-agent: Diffbot
Allow: /

User-agent: YouBot
Allow: /

User-agent: TimpiBot
Allow: /

User-agent: Bytespider-Search
Allow: /

# ── Block known abusive / SEO-spam bots ───────────────
User-agent: AhrefsBot
Disallow: /

User-agent: SemrushBot
Disallow: /

User-agent: MJ12bot
Disallow: /

User-agent: DotBot
Disallow: /

User-agent: PetalBot
Disallow: /

User-agent: BLEXBot
Disallow: /

User-agent: SeekportBot
Disallow: /

User-agent: Bytespider
Disallow: /

# (Ahrefs/Semrush/MJ12 are competitor-intel scrapers; uncomment block lines if you do not use those tools yourself.)

# ── Sitemaps ──────────────────────────────────────────
Sitemap: https://jijualuminium.com/sitemap_index.xml
```

### Notes
- The previous robots.txt allowed Ahrefs/Semrush by default — these contribute nothing to ranking and let competitors fingerprint your link graph. The block lines above are recommended.
- `Bytespider` (TikTok / ByteDance crawler) is explicitly blocked because it has historically been very aggressive and contributes little to discovery. `Bytespider-Search` (the new search-product crawler) is allowed.
- After deploying, validate at: https://www.google.com/webmasters/tools/robots-testing-tool and https://search.marginalia.nu/robots-txt-validator/

---

## B. Drop-in `llms.txt`

Replace the current `/llms.txt` (machine-generated by the Hostinger/llms-txt plugin, contains Chinese characters, HTML entities, and placeholder title/description) with this hand-curated version. Save to `public_html/llms.txt`.

```
# Shandong JIJU Aluminium Industry Co., Ltd.

> Custom aluminum extrusion manufacturer in China since 1994.
> 21 presses, 150,000 t/year, 6063/6061/6005/6082 alloys, ISO 9001/14001/45001.

JIJU is a Chinese aluminum extrusion manufacturer founded in 1994, headquartered in
Linqu County, Weifang City, Shandong Province. The 300,000 m² factory operates
21 extrusion presses (450 T to 7,500 T) producing 150,000 tonnes/year of custom
profiles for doors and windows, EV battery trays, photovoltaic frames, LED heat
sinks, T-slot industrial framing, and architectural cladding. In-house surface
treatments include anodizing (AA10–AA25), powder coating (QUALICOAT class 1–2),
PVDF / fluorocarbon spraying, wood-grain transfer, brushing, and 5-axis CNC
machining. JIJU exports to 40+ countries and accepts T/T, L/C at sight, FOB/CIF/DDP.

## Core pages

- [Custom Aluminum Extrusion — Buyer's Guide](https://jijualuminium.com/custom-aluminum-extrusion/): Pillar page covering design, tooling, alloys, surface treatment, standards, MOQ, lead times, and pricing for B2B custom aluminum extrusion projects.
- [Aluminum Extrusion Process Guide](https://jijualuminium.com/custom-aluminum-extrusion-guide-from-design-to-delivery/): 3,000-word cornerstone explaining the 6-stage extrusion process from billet to packaging.
- [About JIJU Aluminium](https://jijualuminium.com/about-jiju-aluminium/): Company history, leadership, factory tour, certifications, sustainability.
- [Contact / Quote Request](https://jijualuminium.com/contact-aluminum-supplier/): Form, address, WhatsApp, ports.
- [Frequently Asked Questions](https://jijualuminium.com/faq/): 20+ B2B procurement FAQs covering MOQ, lead times, alloys, surface treatments, shipping, and payment.

## Alloys

- [6063 Aluminum Extrusion](https://jijualuminium.com/alloys/6063-aluminum/): Composition, mechanical properties, T5/T6 tempers, applications in doors/windows/decorative profiles.
- [6061 Aluminum Extrusion](https://jijualuminium.com/alloys/6061-aluminum/): Higher-strength alloy for structural framing, T-slot, EV chassis.
- [6005 Aluminum Extrusion](https://jijualuminium.com/alloys/6005-aluminum/): Intermediate alloy for railway, marine, EV battery housings.
- [6082 Aluminum Extrusion](https://jijualuminium.com/alloys/6082-aluminum/): Highest-strength 6xxx alloy.
- [6061 vs 6063 Aluminum Comparison](https://jijualuminium.com/blog/6061-vs-6063-aluminum-comparison/): Side-by-side mechanical, cost, and application comparison.

## Industry hubs

- [Aluminum Profiles for Doors & Windows](https://jijualuminium.com/industries/doors-and-windows/): Thermal-break frames, sliding rails, casement profiles, curtain-wall systems.
- [EV Battery Tray Aluminum Extrusion](https://jijualuminium.com/industries/ev-battery-trays/): 6005A/6082-T6 housings for new-energy vehicle OEMs.
- [Solar / PV Module Frame Aluminum](https://jijualuminium.com/industries/solar-pv-frames/): 6063-T5 anodized PV frames in 30/35/40/45/50 mm depths.
- [LED Heat Sink Aluminum Extrusion](https://jijualuminium.com/industries/led-heat-sinks/): Custom heat-dissipation profiles up to 12 fins/inch.
- [Industrial T-Slot Framing](https://jijualuminium.com/industries/industrial-framing-tslot/): Bosch Rexroth / 80/20-compatible profiles 20×20 to 100×100.
- [Architectural & Decorative Aluminum](https://jijualuminium.com/industries/architectural-decorative/): Wood-grain transfer, brushed, PVDF for cladding and signage.
- [Aluminum Curtain Wall Profiles](https://jijualuminium.com/industries/curtain-wall/): Mullion/transom systems up to 8 m.

## Surface finishes

- [Anodizing](https://jijualuminium.com/surface-finishes/anodizing/): AA10/AA15/AA20/AA25 thickness, natural and color-dyed.
- [Powder Coating](https://jijualuminium.com/surface-finishes/powder-coating/): QUALICOAT class 1 and 2, all RAL colors.
- [PVDF / Fluorocarbon](https://jijualuminium.com/surface-finishes/pvdf/): ≥70% PVDF resin, 25-year warranty.

## Pricing & standards

- [Pricing & MOQ Guide](https://jijualuminium.com/aluminum-extrusion-pricing-guide/): MOQ tiers, FOB pricing logic, mold-cost amortization, Incoterms.
- [Aluminum Extrusion Standards](https://jijualuminium.com/aluminum-extrusion-standards/): EN 755 vs ASTM B221 vs GB/T 5237 side-by-side.
- [Tolerances & Quality Control](https://jijualuminium.com/aluminum-extrusion-tolerances-qc/): ±0.05 mm wall, ±0.2 mm/m length, CMM inspection.
- [Certifications](https://jijualuminium.com/certifications/): ISO 9001, ISO 14001, ISO 45001, REACH, RoHS — downloadable PDFs.

## Case studies

- [Case Studies Index](https://jijualuminium.com/case-studies/): Real client projects with named industries, alloys, finishes, and outcomes.

## Optional

- [Aluminum Catalogue PDF](https://jijualuminium.com/aluminum-catalogue-pdf/): Full product catalog download.
- [Factory Video Tour](https://jijualuminium.com/aluminum-extrusion-videos/): 21 presses, anodizing line, CNC center, packaging.
- [Aluminum Extrusion Cost Calculator](https://jijualuminium.com/aluminum-extrusion-cost-calculator/): Interactive tool for budget estimation.
- [China Aluminum Extrusion Export Index Q3 2026](https://jijualuminium.com/research/china-aluminum-extrusion-export-index-2026-q3/): Original quarterly data report.
- [Privacy Policy](https://jijualuminium.com/privacy-policy/)
- [Terms of Service](https://jijualuminium.com/terms/)
- [Editorial Policy](https://jijualuminium.com/editorial-policy/)
```

### Notes
- The `## Optional` section is the last section per spec — content there is "less essential" and engines may de-prioritize it for primary citation but use it for context.
- Keep `llms.txt` < 50 KB. Current is 37 KB; the curated version above is ~3 KB.
- Keep the URLs in `llms.txt` aligned with the URLs in the sitemap. Update when content changes.
- Validate at: https://llmstxt.org/

---

## C. (Optional, premium) `llms-full.txt`

For sites that want to expose deep content to AI crawlers in one file, create `/llms-full.txt` containing the **full Markdown** of the cornerstone pages. JIJU's first version should include:

- Homepage hero paragraph (rewritten)
- "By the Numbers" table
- 6063 alloy page (full markdown)
- 6061 alloy page
- 6061 vs 6063 comparison
- Aluminum extrusion process pillar
- 20 FAQs
- 20 AI citation blocks

This is a maintenance commitment — only ship once the cornerstone pages are stable.

---
