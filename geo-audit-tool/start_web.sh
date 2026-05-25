#!/bin/bash
# 启动 GEO+SEO 审计 Web 界面
cd "$(dirname "$0")"
export PYTHONPATH="${PWD}:${PYTHONPATH}"

if [ -d ".venv" ]; then
  source .venv/bin/activate
fi

pip install -q -r requirements.txt 2>/dev/null

echo ""
echo "  GEO + SEO 审计 Web 界面"
echo "  打开浏览器: http://127.0.0.1:8765"
echo "  按 Ctrl+C 停止"
echo ""

exec python3 -m uvicorn web.app:app --host 0.0.0.0 --port 8765 --reload
