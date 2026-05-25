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
