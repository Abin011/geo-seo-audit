# GEO+SEO 审计 Web 界面（Windows PowerShell 一键启动）
# 用法：
#   cd geo-audit-tool
#   .\start_web.ps1

Set-Location -Path $PSScriptRoot
$env:PYTHONPATH = (Get-Location).Path

Write-Host ""
Write-Host "GEO + SEO 审计 Web 界面" -ForegroundColor Cyan
Write-Host "浏览器打开: http://127.0.0.1:8765" -ForegroundColor Yellow
Write-Host "按 Ctrl+C 停止"
Write-Host ""

python -m pip install -r requirements.txt
python -m uvicorn web.app:app --host 127.0.0.1 --port 8765 --reload
