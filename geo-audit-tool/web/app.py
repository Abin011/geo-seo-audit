# -*- coding: utf-8 -*-
"""
GEO + SEO 审计 Web 界面

启动:
  cd /Users/abin/SEO/geo-audit-tool
  pip install -r requirements.txt
  pip install fastapi uvicorn
  python -m uvicorn web.app:app --reload --host 0.0.0.0 --port 8765

浏览器打开: http://127.0.0.1:8765
"""

from __future__ import annotations

import threading
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from web.jobs import JobStatus, create_job, get_job
from web.worker import run_job

APP_ROOT = Path(__file__).resolve().parent
STATIC_DIR = APP_ROOT / "static"
OUTPUT_ROOT = APP_ROOT.parent / "output" / "web"
OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

app = FastAPI(
    title="GEO + SEO 审计工具",
    description="外贸 B2B 独立站 SEO/GEO 自动诊断（中文报告）",
    version="1.0.0",
)

if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


class AuditRequest(BaseModel):
    url: str = Field(..., description="待审计网站 URL", examples=["https://jijualuminium.com"])
    max_pages: int = Field(50, ge=10, le=100)
    samples: int = Field(6, ge=2, le=15)


@app.get("/", response_class=HTMLResponse)
async def index() -> HTMLResponse:
    html_path = STATIC_DIR / "index.html"
    if not html_path.exists():
        raise HTTPException(500, "index.html 缺失")
    return HTMLResponse(html_path.read_text(encoding="utf-8"))


@app.post("/api/audit")
async def start_audit(req: AuditRequest) -> JSONResponse:
    url = req.url.strip()
    if not url:
        raise HTTPException(400, "请输入 URL")
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    job = create_job(url)
    thread = threading.Thread(
        target=run_job,
        args=(job.id, url, OUTPUT_ROOT, req.max_pages, req.samples),
        daemon=True,
    )
    thread.start()
    return JSONResponse({"job_id": job.id, "status": job.status.value})


@app.get("/api/status/{job_id}")
async def job_status(job_id: str) -> JSONResponse:
    job = get_job(job_id)
    if not job:
        raise HTTPException(404, "任务不存在或已过期")
    return JSONResponse(job.to_dict())


@app.get("/report/{job_id}", response_class=HTMLResponse)
async def view_report(job_id: str) -> HTMLResponse:
    job = get_job(job_id)
    if not job:
        raise HTTPException(404, "任务不存在")
    if job.status != JobStatus.DONE or not job.report_html:
        raise HTTPException(400, "报告尚未生成完成")
    return HTMLResponse(job.report_html)


@app.get("/api/download/{job_id}/{fmt}")
async def download_report(job_id: str, fmt: str) -> FileResponse:
    job = get_job(job_id)
    if not job or not job.output_dir:
        raise HTTPException(404, "任务不存在")
    out = Path(job.output_dir)
    files = list(out.glob("*"))
    if fmt == "md":
        candidates = [f for f in files if f.suffix == ".md"]
    elif fmt == "html":
        candidates = [f for f in files if f.suffix == ".html"]
    elif fmt == "json":
        candidates = [f for f in files if f.suffix == ".json"]
    else:
        raise HTTPException(400, "格式仅支持 md / html / json")
    if not candidates:
        raise HTTPException(404, "文件未找到")
    path = candidates[0]
    media = {
        "md": "text/markdown",
        "html": "text/html",
        "json": "application/json",
    }[fmt]
    return FileResponse(path, media_type=media, filename=path.name)
