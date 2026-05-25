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
