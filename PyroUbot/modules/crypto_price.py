from PyroUbot import *
import aiohttp
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ᴄʀʏᴘᴛᴏ"
__HELP__ = """
<blockquote><b>💰 Bantuan Crypto Price Tracker

⌬ perintah: <code>{0}crypto [symbol]</code>
⊷ Cek harga cryptocurrency real-time
⊷ Contoh: <code>{0}crypto BTC</code> atau <code>{0}crypto ETH</code>

⌬ perintah: <code>{0}cryptolist</code>
⊷ Lihat daftar crypto populer yang didukung</b></blockquote>
"""

POPULAR_CRYPTOS = {
    "BTC": "Bitcoin",
    "ETH": "Ethereum",
    "BNB": "Binance Coin",
    "SOL": "Solana",
    "XRP": "Ripple",
    "ADA": "Cardano",
    "DOGE": "Dogecoin",
    "TRX": "Tron",
    "MATIC": "Polygon",
    "DOT": "Polkadot"
}

@PY.UBOT("crypto")
@PY.TOP_CMD
async def crypto_price(client, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji> Mohon gunakan format:\n<code>.crypto [SYMBOL]</code>\n\nContoh: <code>.crypto BTC</code>"
            )
            return
        
        symbol = message.command[1].upper()
        prs = await message.reply_text(f"<emoji id=6226405134004389590>🔍</emoji> Mengecek harga {symbol}...")
        
        async with aiohttp.ClientSession() as session:
            # Try CoinGecko API first
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol.lower()}&vs_currencies=usd,idr&include_24hr_change=true&include_market_cap=true"
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    if data:
                        crypto_id = list(data.keys())[0]
                        info = data[crypto_id]
                        
                        price_usd = info.get('usd', 0)
                        price_idr = info.get('idr', 0)
                        change_24h = info.get('usd_24h_change', 0)
                        market_cap = info.get('usd_market_cap', 0)
                        
                        change_emoji = "📈" if change_24h > 0 else "📉"
                        change_color = "+" if change_24h > 0 else ""
                        
                        text = f"""
<blockquote><b>💰 Crypto Price: {symbol.upper()}</b></blockquote>

<blockquote><b>💵 Price USD:</b> ${price_usd:,.2f}
<b>💸 Price IDR:</b> Rp {price_idr:,.0f}

<b>{change_emoji} 24h Change:</b> {change_color}{change_24h:.2f}%
<b>📊 Market Cap:</b> ${market_cap:,.0f}</blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
                        await prs.edit(text)
                        return
            
            # Fallback to alternative API
            url2 = f"https://api.coingecko.com/api/v3/coins/{symbol.lower()}"
            async with session.get(url2) as resp2:
                if resp2.status == 200:
                    data = await resp2.json()
                    price_usd = data['market_data']['current_price']['usd']
                    price_idr = data['market_data']['current_price']['idr']
                    change_24h = data['market_data']['price_change_percentage_24h']
                    market_cap = data['market_data']['market_cap']['usd']
                    
                    change_emoji = "📈" if change_24h > 0 else "📉"
                    change_color = "+" if change_24h > 0 else ""
                    
                    text = f"""
<blockquote><b>💰 Crypto Price: {symbol.upper()}</b></blockquote>

<blockquote><b>💵 Price USD:</b> ${price_usd:,.2f}
<b>💸 Price IDR:</b> Rp {price_idr:,.0f}

<b>{change_emoji} 24h Change:</b> {change_color}{change_24h:.2f}%
<b>📊 Market Cap:</b> ${market_cap:,.0f}</blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
                    await prs.edit(text)
                    return
        
        await prs.edit(f"<emoji id=5019523782004441717>❌</emoji> Crypto {symbol} tidak ditemukan!\n\nGunakan <code>.cryptolist</code> untuk melihat daftar crypto populer.")
        
    except Exception as e:
        await message.reply_text(f"<emoji id=5019523782004441717>❌</emoji> Error: {str(e)}")

@PY.UBOT("cryptolist")
@PY.TOP_CMD
async def crypto_list(client, message: Message):
    text = "<blockquote><b>💰 Crypto Populer yang Didukung:</b></blockquote>\n\n"
    for symbol, name in POPULAR_CRYPTOS.items():
        text += f"<blockquote><b>• {symbol}</b> - {name}</blockquote>\n"
    text += "\n<blockquote><b>Gunakan:</b> <code>.crypto [SYMBOL]</code></blockquote>"
    text += "\n\n<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>"
    await message.reply_text(text)

@PY.BOT("crypto")
async def crypto_price_bot(client, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text(
                "<blockquote><b><emoji id=5019523782004441717>❌</emoji> Mohon gunakan format:\n<code>/crypto [SYMBOL]</code>\n\nContoh: <code>/crypto BTC</code></b></blockquote>"
            )
            return
        
        symbol = message.command[1].upper()
        prs = await message.reply_text(f"<blockquote><b><emoji id=6226405134004389590>🔍</emoji> Mengecek harga {symbol}...</b></blockquote>")
        
        async with aiohttp.ClientSession() as session:
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol.lower()}&vs_currencies=usd,idr&include_24hr_change=true&include_market_cap=true"
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    if data:
                        crypto_id = list(data.keys())[0]
                        info = data[crypto_id]
                        
                        price_usd = info.get('usd', 0)
                        price_idr = info.get('idr', 0)
                        change_24h = info.get('usd_24h_change', 0)
                        market_cap = info.get('usd_market_cap', 0)
                        
                        change_emoji = "📈" if change_24h > 0 else "📉"
                        change_color = "+" if change_24h > 0 else ""
                        
                        text = f"""
<blockquote><b>💰 Crypto Price: {symbol.upper()}</b></blockquote>

<blockquote><b>💵 Price USD:</b> ${price_usd:,.2f}
<b>💸 Price IDR:</b> Rp {price_idr:,.0f}

<b>{change_emoji} 24h Change:</b> {change_color}{change_24h:.2f}%
<b>📊 Market Cap:</b> ${market_cap:,.0f}</blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
                        await prs.edit(text)
                        return
        
        await prs.edit(f"<blockquote><b><emoji id=5019523782004441717>❌</emoji> Crypto {symbol} tidak ditemukan!</b></blockquote>")
        
    except Exception as e:
        await message.reply_text(f"<blockquote><b><emoji id=5019523782004441717>❌</emoji> Error: {str(e)}</b></blockquote>")