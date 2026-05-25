# GEO + SEO 审计工具（中文版）

面向**外贸 B2B 独立站**的自动化 SEO + GEO（生成式引擎优化）诊断程序，支持 CLI 与 Web 界面，**分析报告以中文输出**。

## 功能概览

| 模块 | 说明 |
|---|---|
| 站点发现 | 解析 `sitemap_index.xml` / `sitemap.xml`，最多 50 个 URL |
| 基础 SEO | Title、Meta、H1/H2、Canonical、图片 alt、内链数量 |
| 技术 SEO | TTFB、页面体积、安全响应头、robots.txt、重复 URL 检测 |
| GEO 技术 | AI 爬虫 robots 状态、llms.txt 检测 |
| 结构化数据 | JSON-LD 类型检测（Product / FAQ / Organization 等） |
| 评分模型 | SEO 总分、GEO 总分及 6 项分项（与 geo-audit skill 权重一致） |
| 中文报告 | Markdown + HTML + JSON |
| 可执行交付物 | 首页重写建议、关键词表、Topic Cluster、FAQ/Schema/内链/90天计划模板 |

## 安装

```bash
cd /Users/abin/SEO/geo-audit-tool
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Web 界面（推荐）

```bash
cd /Users/abin/SEO/geo-audit-tool
chmod +x start_web.sh
./start_web.sh
```

浏览器打开 **http://127.0.0.1:8765** → 输入 URL → 等待 1–3 分钟 → 查看/下载中文报告。

或手动启动：

```bash
pip install -r requirements.txt
PYTHONPATH=. python3 -m uvicorn web.app:app --reload --host 0.0.0.0 --port 8765
```

## CLI 使用

```bash
# 基本用法
python main.py https://example.com

# 指定输出目录与抽样深度
python main.py https://example.com -o ./reports --max-pages 50 --samples 8

# 安静模式（少打印进度）
python main.py https://example.com -q
```

## 输出文件

在 `-o` 目录下生成：

- `{域名}-GEO-SEO-审计报告.md` — 完整中文 Markdown
- `{域名}-GEO-SEO-审计报告.html` — 可在浏览器打开
- `{域名}-audit-data.json` — 分数与问题列表（便于对接 CMS/看板）

## 项目结构

```
geo-audit-tool/
├── main.py                 # CLI 入口
├── start_web.sh            # 一键启动 Web
├── requirements.txt
├── README.md
├── web/
│   ├── app.py              # FastAPI 服务
│   ├── jobs.py             # 任务状态
│   ├── worker.py           # 后台审计
│   └── static/             # 前端页面
│       ├── index.html
│       ├── style.css
│       └── app.js
└── geo_audit/
    ├── fetch.py            # 抓取、robots、llms、sitemap
    ├── analyzers.py        # 规则引擎 + 评分
    ├── runner.py           # 审计流程编排
    └── report_zh.py        # 中文报告生成
```

## 与 Cursor GEO Skill 的关系

本工具实现的是 **geo-audit skill 的「可本地化运行子集」**：

- ✅ 自动抓取、技术/On-page/Schema/GEO 规则检测、中文报告
- ✅ 评分公式与 90 天计划、交付物模板
- ⏳ 竞品对标、品牌提及扫描、20 条定制 FAQ 全文 — 需接 LLM API 或 Cursor Agent 扩展（见下方）

## 扩展建议（二期）

1. **`--llm`**：调用 OpenAI/Claude API 生成行业定制 FAQ、AI 引用块、竞品分析（中文）
2. **`--pdf`**：复用 `~/.claude/skills/geo/scripts/generate_pdf_report.py`
3. **`--competitors`**：自动抓取竞品首页对比
4. **Web UI**：FastAPI + 上传 URL 一键出报告
5. **WordPress 插件**：审计结果写回 Yoast 建议字段

预期单次审计耗时约 1–3 分钟（取决于抽样页面数与网络）。

## 免责声明

评分为基于页面抓取的**规则估算**，非 Google Search Console / PageSpeed Insights 官方数据。执行优化前请人工核对工厂数据、认证编号等事实性内容。
