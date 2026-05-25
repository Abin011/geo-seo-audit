# SEO / GEO 工作区

## 项目说明

| 目录 | 说明 |
|---|---|
| [`geo-audit-tool/`](geo-audit-tool/) | **GEO + SEO 审计程序**（CLI + Web 界面，中文报告） |
| [`jijualuminium/`](jijualuminium/) | 示例站点 `jijualuminium.com` 的完整审计交付物（报告、Schema、关键词等） |

## 快速开始（审计工具）

```bash
cd geo-audit-tool
pip install -r requirements.txt

# Web 界面
./start_web.sh
# 浏览器打开 http://127.0.0.1:8765

# 或命令行
python main.py https://example.com -o ./output
```

详见 [geo-audit-tool/README.md](geo-audit-tool/README.md)。
