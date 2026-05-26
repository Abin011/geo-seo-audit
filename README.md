# SEO / GEO 工作区

## 项目说明

| 目录 | 说明 |
|---|---|
| [`geo-audit-tool/`](geo-audit-tool/) | **GEO + SEO 审计程序**（CLI + Web 界面，中文报告） |

## 快速开始（审计工具）

### macOS / Linux

```bash
cd geo-audit-tool
pip install -r requirements.txt

# Web 界面
./start_web.sh
# 浏览器打开 http://127.0.0.1:8765

# 或命令行
python main.py https://example.com -o ./output
```

### Windows（CMD）

```bat
cd geo-audit-tool
pip install -r requirements.txt

start_web.bat
REM 浏览器打开 http://127.0.0.1:8765
```

### Windows（PowerShell）

```powershell
cd geo-audit-tool
pip install -r requirements.txt

.\start_web.ps1
```

详见 [geo-audit-tool/README.md](geo-audit-tool/README.md)。
