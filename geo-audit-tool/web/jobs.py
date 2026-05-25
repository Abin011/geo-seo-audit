# -*- coding: utf-8 -*-
"""内存任务队列（单进程开发用；生产可换 Redis）。"""

from __future__ import annotations

import threading
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any


class JobStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    DONE = "done"
    FAILED = "failed"


@dataclass
class AuditJob:
    id: str
    url: str
    status: JobStatus = JobStatus.PENDING
    progress: int = 0
    message: str = "等待开始…"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    finished_at: str | None = None
    output_dir: str | None = None
    scores: dict[str, int] = field(default_factory=dict)
    issue_count: int = 0
    pages_analyzed: int = 0
    report_html: str | None = None
    report_md: str | None = None
    error: str | None = None
    logs: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "url": self.url,
            "status": self.status.value,
            "progress": self.progress,
            "message": self.message,
            "created_at": self.created_at,
            "finished_at": self.finished_at,
            "scores": self.scores,
            "issue_count": self.issue_count,
            "pages_analyzed": self.pages_analyzed,
            "error": self.error,
            "logs": self.logs[-20:],
            "has_report": self.report_html is not None,
        }


_lock = threading.Lock()
_jobs: dict[str, AuditJob] = {}


def create_job(url: str) -> AuditJob:
    job_id = uuid.uuid4().hex[:12]
    job = AuditJob(id=job_id, url=url)
    with _lock:
        _jobs[job_id] = job
    return job


def get_job(job_id: str) -> AuditJob | None:
    with _lock:
        return _jobs.get(job_id)


def update_job(job_id: str, **kwargs: Any) -> None:
    with _lock:
        job = _jobs.get(job_id)
        if job:
            for k, v in kwargs.items():
                setattr(job, k, v)


def append_log(job_id: str, line: str) -> None:
    with _lock:
        job = _jobs.get(job_id)
        if job:
            job.logs.append(line)


def cleanup_old_jobs(max_jobs: int = 50) -> None:
    with _lock:
        if len(_jobs) <= max_jobs:
            return
        sorted_ids = sorted(
            _jobs.keys(),
            key=lambda i: _jobs[i].created_at,
        )
        for jid in sorted_ids[: len(_jobs) - max_jobs]:
            del _jobs[jid]
