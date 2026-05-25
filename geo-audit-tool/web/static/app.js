(function () {
  const $ = (sel) => document.querySelector(sel);

  const formSection = $("#form-section");
  const progressSection = $("#progress-section");
  const resultSection = $("#result-section");
  const errorSection = $("#error-section");

  const form = $("#audit-form");
  const btnSubmit = $("#btn-submit");
  const progressBar = $("#progress-bar");
  const progressMsg = $("#progress-msg");
  const progressUrl = $("#progress-url");
  const logList = $("#log-list");

  let pollTimer = null;
  let currentJobId = null;

  function ratingLabel(score) {
    if (score >= 90) return "优秀";
    if (score >= 75) return "良好";
    if (score >= 60) return "中等";
    if (score >= 40) return "较差";
    return "危急";
  }

  function showOnly(section) {
    [formSection, progressSection, resultSection, errorSection].forEach((el) => {
      el.classList.add("hidden");
    });
    section.classList.remove("hidden");
  }

  function stopPoll() {
    if (pollTimer) {
      clearInterval(pollTimer);
      pollTimer = null;
    }
  }

  async function pollStatus(jobId) {
    try {
      const res = await fetch(`/api/status/${jobId}`);
      if (!res.ok) throw new Error(await res.text());
      const data = await res.json();

      progressBar.style.width = `${data.progress || 0}%`;
      progressMsg.textContent = data.message || "处理中…";

      logList.innerHTML = "";
      (data.logs || []).forEach((line) => {
        const li = document.createElement("li");
        li.textContent = line;
        logList.appendChild(li);
      });
      logList.scrollTop = logList.scrollHeight;

      if (data.status === "done") {
        stopPoll();
        showResult(jobId, data);
      } else if (data.status === "failed") {
        stopPoll();
        showError(data.error || "未知错误");
      }
    } catch (err) {
      stopPoll();
      showError(err.message);
    }
  }

  function showResult(jobId, data) {
    const seo = data.scores?.["SEO总分"] ?? data.scores?.SEO ?? "—";
    const geo = data.scores?.["GEO总分"] ?? data.scores?.GEO ?? "—";

    $("#score-seo").textContent = seo;
    $("#score-geo").textContent = geo;
    $("#rating-seo").textContent = typeof seo === "number" ? ratingLabel(seo) : "";
    $("#rating-geo").textContent = typeof geo === "number" ? ratingLabel(geo) : "";

    $("#meta-issues").textContent = `发现问题 ${data.issue_count ?? 0} 条`;
    $("#meta-pages").textContent = `分析页面 ${data.pages_analyzed ?? 0} 个`;

    const sub = $("#sub-scores");
    sub.innerHTML = "";
    const skip = new Set(["SEO总分", "GEO总分"]);
    Object.entries(data.scores || {}).forEach(([k, v]) => {
      if (skip.has(k)) return;
      const div = document.createElement("div");
      div.className = "sub-item";
      div.innerHTML = `<span>${k}</span><span>${v}</span>`;
      sub.appendChild(div);
    });

    $("#btn-view").href = `/report/${jobId}`;
    $("#btn-md").href = `/api/download/${jobId}/md`;
    $("#btn-html").href = `/api/download/${jobId}/html`;
    $("#btn-json").href = `/api/download/${jobId}/json`;

    showOnly(resultSection);
    btnSubmit.disabled = false;
  }

  function showError(msg) {
    $("#error-text").textContent = msg;
    showOnly(errorSection);
    btnSubmit.disabled = false;
  }

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    stopPoll();

    const url = $("#url").value.trim();
    const max_pages = parseInt($("#max_pages").value, 10) || 50;
    const samples = parseInt($("#samples").value, 10) || 6;

    btnSubmit.disabled = true;
    progressBar.style.width = "0%";
    progressMsg.textContent = "正在提交任务…";
    progressUrl.textContent = url;
    logList.innerHTML = "";
    showOnly(progressSection);

    try {
      const res = await fetch("/api/audit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url, max_pages, samples }),
      });
      if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        throw new Error(err.detail || res.statusText);
      }
      const { job_id } = await res.json();
      currentJobId = job_id;
      pollTimer = setInterval(() => pollStatus(job_id), 1200);
      pollStatus(job_id);
    } catch (err) {
      showError(err.message);
    }
  });

  $("#btn-new").addEventListener("click", () => {
    stopPoll();
    showOnly(formSection);
    btnSubmit.disabled = false;
  });

  $("#btn-retry").addEventListener("click", () => {
    showOnly(formSection);
    btnSubmit.disabled = false;
  });
})();
