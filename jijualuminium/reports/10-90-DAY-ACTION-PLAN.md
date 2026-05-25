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
