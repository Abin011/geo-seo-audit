#!/usr/bin/env python3
"""Build a single, self-contained, professionally styled HTML report from the master markdown."""

import sys
sys.path.insert(0, '/Users/abin/Library/Python/3.9/lib/python/site-packages')

import markdown
import re
from pathlib import Path

REPORT_DIR = Path('/Users/abin/SEO/jijualuminium')
MASTER_MD = REPORT_DIR / 'JIJU-MASTER-REPORT.md'
OUT_HTML = REPORT_DIR / 'JIJU-GEO-SEO-REPORT.html'

md_text = MASTER_MD.read_text(encoding='utf-8')

# Convert markdown to HTML
md = markdown.Markdown(extensions=['extra', 'tables', 'fenced_code', 'toc', 'sane_lists'])
body_html = md.convert(md_text)

# Score gauge SVG generator (donut style)
def gauge_svg(score, label, max_score=100, size=160):
    pct = score / max_score
    angle = pct * 360
    # Color buckets
    if score >= 75: color = '#10b981'   # green
    elif score >= 60: color = '#84cc16' # lime
    elif score >= 40: color = '#f59e0b' # amber
    else: color = '#ef4444'             # red
    radius = size * 0.42
    cx = cy = size / 2
    # SVG arc
    import math
    rad = math.radians(angle - 90)
    end_x = cx + radius * math.cos(rad)
    end_y = cy + radius * math.sin(rad)
    large_arc = 1 if angle > 180 else 0
    arc_path = f"M {cx} {cy - radius} A {radius} {radius} 0 {large_arc} 1 {end_x:.2f} {end_y:.2f}" if angle > 0 else ""
    return f'''
    <div class="gauge">
      <svg viewBox="0 0 {size} {size}" width="{size}" height="{size}">
        <circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="#e5e7eb" stroke-width="14"/>
        <path d="{arc_path}" fill="none" stroke="{color}" stroke-width="14" stroke-linecap="round"/>
        <text x="{cx}" y="{cy + 6}" text-anchor="middle" font-size="36" font-weight="800" fill="#0f172a">{score}</text>
        <text x="{cx}" y="{cy + 28}" text-anchor="middle" font-size="11" fill="#64748b">/ {max_score}</text>
      </svg>
      <div class="gauge-label">{label}</div>
    </div>'''

# Bar chart for category scores
def bar_chart_html(rows):
    out = ['<div class="bar-chart">']
    for label, current, target in rows:
        cur_pct = current
        tgt_pct = target
        if current >= 75: cur_color = '#10b981'
        elif current >= 60: cur_color = '#84cc16'
        elif current >= 40: cur_color = '#f59e0b'
        else: cur_color = '#ef4444'
        out.append(f'''
        <div class="bar-row">
          <div class="bar-label">{label}</div>
          <div class="bar-track">
            <div class="bar-target" style="width:{tgt_pct}%"></div>
            <div class="bar-current" style="width:{cur_pct}%; background:{cur_color}"></div>
          </div>
          <div class="bar-values"><span class="cur">{current}</span><span class="arrow">→</span><span class="tgt">{target}</span></div>
        </div>''')
    out.append('</div>')
    return '\n'.join(out)

# Build cover page
cover_html = f'''
<section class="cover">
  <div class="cover-header">
    <div class="brand-tag">GEO + SEO MASTER AUDIT</div>
    <h1 class="cover-title">JIJU Aluminium</h1>
    <div class="cover-sub">Shandong JIJU Aluminium Industry Co., Ltd.<br/>
      <a href="https://jijualuminium.com/" target="_blank">jijualuminium.com</a></div>
    <div class="cover-meta">
      Audit date: <strong>25 May 2026</strong> · 
      Industry: <strong>B2B Custom Aluminum Extrusion (foreign-trade independent site)</strong> · 
      Tech: WordPress · WooCommerce · Yoast · Hostinger
    </div>
  </div>

  <div class="cover-scores">
    {gauge_svg(42, 'SEO Score', size=200)}
    {gauge_svg(37, 'GEO Score', size=200)}
  </div>

  <div class="cover-projection">
    <h3>Projected 90-day Uplift (full-execution scenario)</h3>
    <div class="projection-grid">
      <div class="proj-card"><div class="proj-num">+60–90 %</div><div class="proj-label">Google organic traffic</div></div>
      <div class="proj-card"><div class="proj-num">+250–400 %</div><div class="proj-label">AI search exposure / citations</div></div>
      <div class="proj-card"><div class="proj-num">+35–65 %</div><div class="proj-label">Inquiry / quote-request volume</div></div>
      <div class="proj-card"><div class="proj-num">37 → 78</div><div class="proj-label">Composite GEO score</div></div>
      <div class="proj-card"><div class="proj-num">42 → 80</div><div class="proj-label">Composite SEO score</div></div>
      <div class="proj-card"><div class="proj-num">25 → 65</div><div class="proj-label">Brand authority score</div></div>
    </div>
  </div>

  <div class="cover-categories">
    <h3>Category Score Breakdown — current vs. 90-day target</h3>
    {bar_chart_html([
      ("AI Citability (25%)", 35, 80),
      ("Brand Authority (20%)", 25, 65),
      ("Content E-E-A-T (20%)", 30, 75),
      ("Technical GEO (15%)", 58, 85),
      ("Schema & Structured Data (10%)", 58, 92),
      ("Platform Optimization (10%)", 26, 75),
    ])}
  </div>

  <div class="cover-summary">
    <h3>Headline diagnosis</h3>
    <p>JIJU has the <strong>raw material of a tier-1 B2B aluminum extrusion site</strong> — a real 30-year-old factory with verifiable scale (150,000 t/year, 21 presses, 300,000 m², ISO 9001/14001/45001), a cornerstone blog with genuine engineering depth, a 137-product catalog, and a permissive <code>robots.txt</code> that lets every AI bot in. The site is server-rendered, on HTTP/2 + Brotli, and Yoast already emits valid baseline schema.</p>
    <p>Yet today JIJU is <strong>largely invisible to AI search engines</strong> and underperforming on Google for high-intent B2B queries. Six concrete failure modes drive the 37/100 GEO score: (1) edge cache bypassed on every URL · (2) commerce-critical schema (Product, FAQPage, HowTo, LocalBusiness) is missing · (3) no AI entity (no Wikidata QID, no Wikipedia, no LinkedIn company page, non-branded YouTube) · (4) duplicated boilerplate across ~100 product pages plus AI-voice blog content and conflicting factory stats · (5) no <code>hreflang</code> · (6) <code>llms.txt</code> exists but contains placeholders and Chinese-character contamination.</p>
    <p>Every issue is fixable. This report contains the complete remediation package: rewritten homepage copy, 30-keyword strategy, topic cluster map, 20 ready-to-publish FAQs (plus FAQPage schema), 20 AI-quotable citation blocks, a 13-block JSON-LD schema bundle, drop-in <code>robots.txt</code> and <code>llms.txt</code> files, internal-linking map, and a sequenced 90-day action plan totaling ≈72 person-days of effort and ≈USD 6,000 of external cost.</p>
  </div>

  <div class="cover-toc">
    <h3>Report contents</h3>
    <ol>
      <li><a href="#section-1">Executive Summary &amp; Scores</a></li>
      <li><a href="#section-2">Critical Issues (by severity)</a></li>
      <li><a href="#section-3">Page-Level Analysis</a></li>
      <li><a href="#section-4">Competitor Benchmark</a></li>
      <li><a href="#section-5">Rewritten Homepage (copy-paste)</a></li>
      <li><a href="#section-6">Keyword Strategy + Topic Cluster Map</a></li>
      <li><a href="#section-7">20 B2B FAQs (with FAQPage schema)</a></li>
      <li><a href="#section-8">20 AI-Citation Content Blocks</a></li>
      <li><a href="#section-9">Schema Deployment Guide (13 JSON-LD blocks)</a></li>
      <li><a href="#section-10">Internal Linking Map</a></li>
      <li><a href="#section-11">90-Day Action Plan</a></li>
      <li><a href="#section-12">robots.txt + llms.txt (drop-in files)</a></li>
    </ol>
  </div>
</section>
<div class="page-break"></div>
'''

# Add anchor IDs to the H1s in body_html so TOC links work
section_id = [0]
def add_section_id(match):
    section_id[0] += 1
    return f'<h1 id="section-{section_id[0]}">{match.group(1)}</h1>'
body_html = re.sub(r'<h1>([^<]+)</h1>', add_section_id, body_html)

# Full HTML document
html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>JIJU Aluminium — GEO + SEO Master Audit Report (May 2026)</title>
<style>
  * {{ box-sizing: border-box; }}
  html, body {{ margin: 0; padding: 0; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Inter", "Helvetica Neue", Arial, sans-serif;
    color: #0f172a;
    background: #f8fafc;
    line-height: 1.55;
    font-size: 15px;
  }}
  .container {{
    max-width: 1100px;
    margin: 0 auto;
    background: #ffffff;
    box-shadow: 0 1px 4px rgba(15,23,42,0.06);
  }}

  /* COVER */
  .cover {{
    padding: 60px 70px 80px;
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 60%, #334155 100%);
    color: #f1f5f9;
  }}
  .cover-header {{ margin-bottom: 40px; }}
  .brand-tag {{
    font-size: 11px;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #94a3b8;
    margin-bottom: 14px;
    font-weight: 600;
  }}
  .cover-title {{
    font-size: 56px;
    font-weight: 900;
    margin: 0 0 12px 0;
    color: #ffffff;
    letter-spacing: -0.02em;
  }}
  .cover-sub {{
    font-size: 16px;
    color: #cbd5e1;
    margin-bottom: 14px;
  }}
  .cover-sub a {{ color: #38bdf8; text-decoration: none; }}
  .cover-meta {{
    font-size: 13px;
    color: #94a3b8;
    border-top: 1px solid #334155;
    padding-top: 12px;
  }}
  .cover-meta strong {{ color: #e2e8f0; }}

  .cover-scores {{
    display: flex;
    gap: 60px;
    justify-content: center;
    margin: 50px 0 50px;
    padding: 36px;
    background: rgba(255,255,255,0.05);
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.08);
  }}
  .gauge {{ text-align: center; }}
  .gauge svg {{ background: #ffffff; border-radius: 50%; padding: 4px; }}
  .gauge-label {{
    margin-top: 12px;
    font-size: 13px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #cbd5e1;
  }}

  .cover-projection {{ margin-bottom: 40px; }}
  .cover-projection h3, .cover-categories h3, .cover-summary h3, .cover-toc h3 {{
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #38bdf8;
    margin: 0 0 16px;
    font-weight: 700;
  }}
  .projection-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
  }}
  .proj-card {{
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 10px;
    padding: 18px 14px;
    text-align: center;
  }}
  .proj-num {{
    font-size: 26px;
    font-weight: 800;
    color: #fbbf24;
    margin-bottom: 4px;
    letter-spacing: -0.01em;
  }}
  .proj-label {{
    font-size: 12px;
    color: #cbd5e1;
    line-height: 1.3;
  }}

  .cover-categories {{ margin-bottom: 40px; }}
  .bar-chart {{ display: flex; flex-direction: column; gap: 10px; }}
  .bar-row {{
    display: grid;
    grid-template-columns: 220px 1fr 100px;
    align-items: center;
    gap: 14px;
  }}
  .bar-label {{ font-size: 13px; color: #cbd5e1; }}
  .bar-track {{
    position: relative;
    height: 22px;
    background: rgba(255,255,255,0.06);
    border-radius: 5px;
    overflow: hidden;
  }}
  .bar-target {{
    position: absolute;
    top: 0; left: 0; bottom: 0;
    background: rgba(56,189,248,0.18);
    border-right: 2px dashed rgba(56,189,248,0.6);
  }}
  .bar-current {{
    position: absolute;
    top: 0; left: 0; bottom: 0;
    border-radius: 5px;
  }}
  .bar-values {{
    font-size: 13px;
    text-align: right;
    color: #e2e8f0;
    font-variant-numeric: tabular-nums;
  }}
  .bar-values .cur {{ color: #fbbf24; font-weight: 700; }}
  .bar-values .arrow {{ color: #64748b; margin: 0 4px; }}
  .bar-values .tgt {{ color: #38bdf8; font-weight: 700; }}

  .cover-summary p {{
    color: #e2e8f0;
    font-size: 14px;
    line-height: 1.65;
    margin: 0 0 12px;
  }}
  .cover-summary code {{
    background: rgba(56,189,248,0.15);
    color: #7dd3fc;
    padding: 1px 5px;
    border-radius: 3px;
    font-size: 13px;
  }}

  .cover-toc {{ margin-top: 40px; padding-top: 28px; border-top: 1px solid #334155; }}
  .cover-toc ol {{ margin: 0; padding-left: 22px; column-count: 2; column-gap: 30px; }}
  .cover-toc li {{ margin: 4px 0; color: #cbd5e1; }}
  .cover-toc a {{ color: #cbd5e1; text-decoration: none; }}
  .cover-toc a:hover {{ color: #38bdf8; }}

  /* PAGE BREAK */
  .page-break {{ page-break-after: always; height: 0; }}

  /* BODY (sections after cover) */
  .report-body {{
    padding: 40px 70px 80px;
  }}
  .report-body h1 {{
    font-size: 28px;
    color: #0f172a;
    border-bottom: 3px solid #fbbf24;
    padding-bottom: 8px;
    margin: 50px 0 22px;
    letter-spacing: -0.01em;
  }}
  .report-body h1:first-of-type {{ margin-top: 0; }}
  .report-body h2 {{
    font-size: 21px;
    color: #1e293b;
    margin: 32px 0 14px;
    padding-left: 10px;
    border-left: 4px solid #38bdf8;
  }}
  .report-body h3 {{
    font-size: 17px;
    color: #334155;
    margin: 22px 0 10px;
  }}
  .report-body h4 {{
    font-size: 15px;
    color: #475569;
    margin: 16px 0 8px;
  }}
  .report-body p {{ margin: 8px 0; }}
  .report-body strong {{ color: #0f172a; }}
  .report-body em {{ color: #475569; }}
  .report-body a {{ color: #0284c7; text-decoration: none; }}
  .report-body a:hover {{ text-decoration: underline; }}
  .report-body code {{
    background: #f1f5f9;
    padding: 1px 6px;
    border-radius: 3px;
    font-size: 13px;
    color: #be185d;
    font-family: "SF Mono", Menlo, Consolas, monospace;
  }}
  .report-body pre {{
    background: #0f172a;
    color: #e2e8f0;
    padding: 16px 18px;
    border-radius: 6px;
    overflow-x: auto;
    font-size: 12.5px;
    line-height: 1.5;
    margin: 14px 0;
  }}
  .report-body pre code {{
    background: transparent;
    color: inherit;
    padding: 0;
    font-size: 12.5px;
  }}
  .report-body table {{
    border-collapse: collapse;
    width: 100%;
    font-size: 13px;
    margin: 14px 0;
    border: 1px solid #e2e8f0;
  }}
  .report-body th {{
    background: #f1f5f9;
    color: #0f172a;
    text-align: left;
    padding: 8px 10px;
    border-bottom: 2px solid #cbd5e1;
    border-right: 1px solid #e2e8f0;
    font-weight: 700;
    font-size: 12.5px;
  }}
  .report-body td {{
    padding: 8px 10px;
    border-bottom: 1px solid #e2e8f0;
    border-right: 1px solid #e2e8f0;
    vertical-align: top;
  }}
  .report-body tr:hover td {{ background: #f8fafc; }}
  .report-body ul, .report-body ol {{ padding-left: 26px; margin: 8px 0; }}
  .report-body li {{ margin: 4px 0; }}
  .report-body blockquote {{
    border-left: 4px solid #fbbf24;
    background: #fffbeb;
    padding: 14px 18px;
    margin: 14px 0;
    color: #422006;
    border-radius: 0 4px 4px 0;
    font-size: 14px;
  }}
  .report-body hr {{
    border: 0;
    border-top: 1px dashed #cbd5e1;
    margin: 24px 0;
  }}

  /* Severity color cues — applied via CSS keyword detection */
  .report-body table td:first-child {{ font-weight: 700; color: #be123c; }}

  /* Footer */
  .report-footer {{
    background: #0f172a;
    color: #cbd5e1;
    padding: 30px 70px;
    font-size: 12px;
    line-height: 1.7;
  }}
  .report-footer h4 {{ color: #fbbf24; font-size: 13px; margin: 0 0 8px; }}
  .report-footer a {{ color: #38bdf8; }}

  /* Print */
  @media print {{
    body {{ background: #fff; }}
    .container {{ box-shadow: none; max-width: 100%; }}
    .cover {{ padding: 40px; min-height: 90vh; }}
    .report-body {{ padding: 30px 40px; }}
    .report-body h1 {{ page-break-before: always; }}
    .report-body h1:first-of-type {{ page-break-before: avoid; }}
    .report-body table, .report-body pre {{ page-break-inside: avoid; }}
    .page-break {{ page-break-after: always; }}
  }}

  @media (max-width: 800px) {{
    .cover {{ padding: 30px 24px 40px; }}
    .cover-title {{ font-size: 38px; }}
    .cover-scores {{ flex-direction: column; gap: 20px; }}
    .projection-grid {{ grid-template-columns: 1fr 1fr; }}
    .bar-row {{ grid-template-columns: 1fr; }}
    .report-body {{ padding: 24px; }}
    .cover-toc ol {{ column-count: 1; }}
  }}
</style>
</head>
<body>
<div class="container">
{cover_html}

<div class="report-body">
{body_html}
</div>

<div class="report-footer">
  <h4>About this report</h4>
  <p>
    Audit conducted 25 May 2026 by an automated GEO + SEO specialist using the
    Cursor agent skill suite (geo-audit, geo-citability, geo-content, geo-platform-analysis,
    geo-schema, geo-technical, geo-ai-visibility, geo-brand-mentions). All raw HTML inspection
    performed against the live <code>https://jijualuminium.com/</code> deployment as it served
    on 25 May 2026 between 02:33–11:38 UTC.
  </p>
  <h4>Source-of-truth files (in this delivery)</h4>
  <p>
    • <code>JIJU-MASTER-REPORT.md</code> — single concatenated markdown of all 12 sections<br/>
    • <code>reports/00–11-*.md</code> — individual section files (editable)<br/>
    • <code>schema/a–m_*.json</code> — 13 ready-to-deploy JSON-LD blocks (1,022 lines total)<br/>
    • <code>schema/combined_snippet.html</code> — all 13 schemas pre-wrapped in <code>&lt;script type="application/ld+json"&gt;</code> tags (1,629 lines, drop-in)<br/>
    • <code>JIJU-GEO-SEO-REPORT.html</code> — this self-contained styled report (printable)
  </p>
  <h4>Disclaimer</h4>
  <p>
    Score projections are estimates based on observed gaps and historical 90-day uplift seen on
    similar B2B foreign-trade sites after full execution of comparable remediation plans. Actual
    results depend on completeness of execution, content quality, off-page signal velocity, and
    competitor response. KPIs in the 90-day plan should be treated as targets, not guarantees.
  </p>
</div>
</div>
</body>
</html>
'''

OUT_HTML.write_text(html, encoding='utf-8')
print(f"Wrote {OUT_HTML} — {OUT_HTML.stat().st_size:,} bytes")
print(f"Open in browser: file://{OUT_HTML}")
