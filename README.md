# 🤖 Ubot Telegram - Advanced Userbot

Telegram Userbot dengan 200+ fitur lengkap untuk automasi dan utility!

## ✨ Fitur Utama

### 🎯 Core Features
- **AI Chat** - Chat dengan AI menggunakan OpenAI API
- **Broadcast System** - Kirim pesan ke banyak grup/user sekaligus
- **Auto Broadcast** - Broadcast otomatis dengan schedule
- **Payment Integration** - Sistem pembayaran terintegrasi
- **Admin Tools** - Lengkap untuk moderasi grup

### 💎 New Premium Features
- **🪙 Crypto Tracker** - Cek harga cryptocurrency real-time
- **🌤️ Weather Info** - Informasi cuaca lengkap
- **📱 QR Generator** - Generate & read QR code
- **🔗 URL Shortener** - Perpendek URL panjang
- **💬 Quotes Generator** - Quote inspiratif random
- **😂 Meme Generator** - Generate meme lucu

### 🛠️ Utilities
- YouTube Stalking & Download
- Music Recognition (Shazam)
- Image Enhancement (Remini)
- Wallpaper Downloader
- Notes Management
- Tag All Users
- Fake Action
- Games & More!

## 🚀 Quick Setup

### Cara Mudah (Recommended)
```bash
python3 setup.py
```
Script ini akan memandu Anda setup bot dengan mudah!

### Manual Setup
1. Clone repository
```bash
git clone <repo-url>
cd <repo-folder>
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Setup configuration
```bash
cp sample.env .env
nano .env
```

4. Isi konfigurasi:
- `BOT_TOKEN` - Dapatkan dari @BotFather
- `API_ID` & `API_HASH` - Dari https://my.telegram.org
- `OWNER_ID` - User ID Telegram Anda (@userinfobot)
- `MONGO_URL` - MongoDB connection string

5. Jalankan bot
```bash
python3 -m PyroUbot
```

## 📦 Dependencies
- Python 3.8+
- Pyrogram - Telegram MTProto framework
- Motor - Async MongoDB driver
- PyTgCalls - Voice call support
- Pillow - Image processing
- aiohttp - Async HTTP client
- Dan banyak lagi!

## 🎮 Command Examples

### Crypto Tracker
```
.crypto BTC          # Cek harga Bitcoin
.crypto ETH          # Cek harga Ethereum
.cryptolist          # Daftar crypto populer
```

### Weather
```
.weather Jakarta     # Cuaca di Jakarta
.cuaca Surabaya      # Cuaca di Surabaya
```

### QR Code
```
.qr https://t.me/me  # Generate QR code
.qrread              # Read QR (reply ke gambar)
```

### URL Shortener
```
.short https://very-long-url.com/path/to/page
```

### Meme
```
.meme               # Random meme dari Reddit
.makememe TOP | BOT # Custom meme (reply ke foto)
```

### Broadcast
```
.gikes all [text]    # Broadcast ke semua
.gikes group [text]  # Broadcast ke grup saja
.gikes users [text]  # Broadcast ke user saja
.stopg              # Stop broadcast
```

### AI Chat
```
.ai Halo, apa kabar?
.ai Jelaskan tentang Python
```

## 🔧 Auto-Start dengan Supervisor

Bot sudah dikonfigurasi untuk auto-start menggunakan Supervisor:

```bash
# Start bot
sudo supervisorctl start ubot

# Stop bot
sudo supervisorctl stop ubot

# Restart bot
sudo supervisorctl restart ubot

# Check status
sudo supervisorctl status

# View logs
tail -f /var/log/supervisor/ubot.out.log
tail -f /var/log/supervisor/ubot.err.log
```

## 📝 Configuration

### Environment Variables
```env
# Bot Configuration
MAX_BOT = 100                    # Max userbot yang bisa aktif
BOT_TOKEN = your_bot_token       # Bot token dari @BotFather

# Telegram API
API_ID = your_api_id             # Dari my.telegram.org
API_HASH = your_api_hash         # Dari my.telegram.org

# Owner & Developers
OWNER_ID = your_user_id          # User ID owner
DEVS = dev1_id dev2_id           # User ID developers

# Database
MONGO_URL = mongodb_url          # MongoDB connection string

# Optional
BLACKLIST_CHAT = chat1 chat2     # Blacklist chat IDs
LOGS_MAKER_UBOT = log_chat_id    # Log channel/group ID
RMBG_API = removebg_api_key      # Remove.bg API (optional)
```

## 🎯 Features Count

- **Total Modules:** 240+ modules
- **Commands:** 500+ commands
- **Utilities:** 50+ utility features
- **Admin Tools:** 30+ admin commands
- **Fun Features:** 40+ entertainment commands
- **API Integrations:** 20+ external APIs

## 🆘 Support

Jika ada masalah atau pertanyaan:
1. Check logs: `tail -f /var/log/supervisor/ubot.out.log`
2. Restart bot: `sudo supervisorctl restart ubot`
3. Re-setup: `python3 setup.py`

## 📄 License

This project is for educational purposes only.

## 🙏 Credits

- Pyrogram Framework
- PyTgCalls for voice features
- All API providers
- Original Ubot developers

---

**Made with ❤️ for Telegram Userbot Community**

🚀 **Happy Botting!** 🤖

