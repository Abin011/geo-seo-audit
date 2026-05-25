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
