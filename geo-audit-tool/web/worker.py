# -*- coding: utf-8 -*-
"""后台执行审计任务。"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from geo_audit.report_zh import save_reports
from geo_audit.runner import run_audit
from web.jobs import JobStatus, append_log, update_job


def run_job(
    job_id: str,
    url: str,
    output_root: Path,
    max_pages: int = 50,
    samples: int = 6,
) -> None:
    out_dir = output_root / job_id
    out_dir.mkdir(parents=True, exist_ok=True)

    steps = [
        (10, "正在抓取首页…"),
        (25, "解析 robots.txt 与 llms.txt…"),
        (40, "爬取 Sitemap…"),
        (55, "抽样分析页面…"),
        (75, "计算 SEO / GEO 评分…"),
        (90, "生成中文报告…"),
    ]

    def progress_cb(step_idx: int, detail: str = "") -> None:
        if step_idx < len(steps):
            pct, msg = steps[step_idx]
            update_job(job_id, progress=pct, message=msg + (f" {detail}" if detail else ""))
            append_log(job_id, msg)

    try:
        update_job(job_id, status=JobStatus.RUNNING, progress=5, message="审计已开始…")
        append_log(job_id, f"目标 URL: {url}")

        progress_cb(0)
        result = run_audit(
            url,
            max_pages=max_pages,
            sample_extra=samples,
            verbose=False,
        )

        for i in range(1, 5):
            progress_cb(i)

        paths = save_reports(result, out_dir)
        progress_cb(5)

        md_text = paths["markdown"].read_text(encoding="utf-8")
        html_text = paths["html"].read_text(encoding="utf-8")

        update_job(
            job_id,
            status=JobStatus.DONE,
            progress=100,
            message="审计完成",
            finished_at=__import__("datetime").datetime.now().isoformat(),
            output_dir=str(out_dir),
            scores=result.scores,
            issue_count=len(result.issues),
            pages_analyzed=result.pages_analyzed,
            report_html=html_text,
            report_md=md_text,
        )
        append_log(job_id, f"报告已保存: {paths['markdown'].name}")

    except Exception as e:
        update_job(
            job_id,
            status=JobStatus.FAILED,
            progress=0,
            message="审计失败",
            error=str(e),
            finished_at=__import__("datetime").datetime.now().isoformat(),
        )
        append_log(job_id, f"错误: {e}")
