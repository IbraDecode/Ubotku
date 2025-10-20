#!/bin/bash
#
# 🤖 Ubot Telegram - Start Script
# Mudah jalankan bot dengan 1 command!
#

echo "╔══════════════════════════════════════════════════╗"
echo "║                                                  ║"
echo "║        🤖 STARTING UBOT TELEGRAM 🤖             ║"
echo "║                                                  ║"
echo "╚══════════════════════════════════════════════════╝"
echo ""

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "⚠️  File .env tidak ditemukan!"
    echo "📝 Menjalankan setup wizard..."
    python3 setup.py
    echo ""
fi

# Check if supervisor is running
if command -v supervisorctl &> /dev/null; then
    echo "🔧 Starting with Supervisor (auto-restart enabled)..."
    sudo supervisorctl reread
    sudo supervisorctl update
    sudo supervisorctl start ubot
    echo ""
    echo "✅ Bot started successfully!"
    echo ""
    echo "📊 Check status: sudo supervisorctl status"
    echo "📝 View logs: tail -f /var/log/supervisor/ubot.out.log"
    echo "🛑 Stop bot: sudo supervisorctl stop ubot"
else
    echo "🚀 Starting bot directly..."
    python3 -m PyroUbot
fi
