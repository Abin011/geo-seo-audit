#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GEO + SEO 外贸 B2B 独立站审计工具

用法:
  python main.py https://example.com
  python main.py https://jijualuminium.com --max-pages 50 --output ./reports
  python main.py https://example.com --quiet

输出:
  - {域名}-GEO-SEO-审计报告.md   （中文完整报告）
  - {域名}-GEO-SEO-审计报告.html  （浏览器可打开）
  - {域名}-audit-data.json       （结构化数据，可对接其他系统）
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# 确保可导入 geo_audit 包
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from geo_audit.report_zh import save_reports
from geo_audit.runner import run_audit


def main() -> int:
    parser = argparse.ArgumentParser(
        description="GEO + SEO 外贸独立站自动审计（中文报告）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("url", help="待审计网站 URL，如 https://jijualuminium.com")
    parser.add_argument(
        "--output", "-o",
        type=Path,
        default=Path("./output"),
        help="报告输出目录（默认 ./output）",
    )
    parser.add_argument(
        "--max-pages", "-m",
        type=int,
        default=50,
        help="Sitemap 最多解析 URL 数（默认 50）",
    )
    parser.add_argument(
        "--samples", "-s",
        type=int,
        default=6,
        help="除首页外额外抽样分析的页面数（默认 6）",
    )
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="减少进度输出",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("  GEO + SEO 审计工具 v1.0")
    print("=" * 60)

    result = run_audit(
        args.url,
        max_pages=args.max_pages,
        sample_extra=args.samples,
        verbose=not args.quiet,
    )

    paths = save_reports(result, args.output.resolve())

    seo = result.scores.get("SEO总分", 0)
    geo = result.scores.get("GEO总分", 0)

    print()
    print("── 审计完成 ──")
    print(f"  SEO 评分: {seo}/100")
    print(f"  GEO 评分: {geo}/100")
    print(f"  发现问题: {len(result.issues)} 条")
    print(f"  分析页面: {result.pages_analyzed} 个")
    print()
    print("输出文件:")
    for k, p in paths.items():
        print(f"  [{k}] {p}")
    print()
    print("用浏览器打开 HTML 报告即可查看完整中文版。")

    return 0


if __name__ == "__main__":
    sys.exit(main())
