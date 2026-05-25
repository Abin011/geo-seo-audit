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
