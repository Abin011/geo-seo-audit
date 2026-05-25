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
