@echo off
setlocal

REM GEO+SEO 审计 Web 界面（Windows CMD 一键启动）
REM 用法：
REM   cd geo-audit-tool
REM   start_web.bat

cd /d "%~dp0"

REM 让 python 能找到本项目模块
set PYTHONPATH=%CD%

echo.
echo  GEO + SEO 审计 Web 界面
echo  浏览器打开: http://127.0.0.1:8765
echo  按 Ctrl+C 停止
echo.

REM 安装依赖（首次较慢，后续会跳过已安装包）
python -m pip install -r requirements.txt

REM 启动 FastAPI
python -m uvicorn web.app:app --host 127.0.0.1 --port 8765 --reload

endlocal
