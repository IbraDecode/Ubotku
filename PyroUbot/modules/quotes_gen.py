from PyroUbot import *
import aiohttp
import random
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ꜰᴜᴏᴛᴇꜱ"
__HELP__ = """
<blockquote><b>💬 Bantuan Quotes Generator

⌬ perintah: <code>{0}quote</code>
⊷ Dapatkan quote inspiratif random

⌬ perintah: <code>{0}quote [category]</code>
⊷ Kategori: life, success, love, motivational, wisdom
⊷ Contoh: <code>{0}quote motivational</code></b></blockquote>
"""

QUOTES_CATEGORIES = {
    "life": "kehidupan",
    "success": "kesuksesan",
    "love": "cinta",
    "motivational": "motivasi",
    "wisdom": "bijaksana",
    "happiness": "kebahagiaan",
    "inspirational": "inspirasi"
}

@PY.UBOT("quote|quotes")
@PY.TOP_CMD
async def get_quote(client, message: Message):
    try:
        category = "inspirational"
        if len(message.command) > 1:
            category = message.command[1].lower()
        
        prs = await message.reply_text(f"<emoji id=6226405134004389590>🔍</emoji> Mencari quote...")
        
        async with aiohttp.ClientSession() as session:
            # Using API Ninjas Quotes API
            api_url = f"https://api.api-ninjas.com/v1/quotes?category={category}"
            headers = {'X-Api-Key': 'free'}  # Using free tier
            
            # Fallback to Quotable API
            quotable_url = "https://api.quotable.io/random"
            async with session.get(quotable_url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    quote_text = data['content']
                    author = data['author']
                    
                    text = f"""
<blockquote><b>💬 Quote of the Day</b></blockquote>

<blockquote><i>"{quote_text}"</i>

<b>— {author}</b></blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
                    await prs.edit(text)
                    return
        
        await prs.edit(f"<emoji id=5019523782004441717>❌</emoji> Gagal mendapatkan quote!")
        
    except Exception as e:
        await message.reply_text(f"<emoji id=5019523782004441717>❌</emoji> Error: {str(e)}")

@PY.BOT("quote|quotes")
async def get_quote_bot(client, message: Message):
    try:
        prs = await message.reply_text(f"<blockquote><b><emoji id=6226405134004389590>🔍</emoji> Mencari quote...</b></blockquote>")
        
        async with aiohttp.ClientSession() as session:
            quotable_url = "https://api.quotable.io/random"
            async with session.get(quotable_url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    quote_text = data['content']
                    author = data['author']
                    
                    text = f"""
<blockquote><b>💬 Quote of the Day</b></blockquote>

<blockquote><i>"{quote_text}"</i>

<b>— {author}</b></blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
                    await prs.edit(text)
                    return
        
        await prs.edit(f"<blockquote><b><emoji id=5019523782004441717>❌</emoji> Gagal mendapatkan quote!</b></blockquote>")
        
    except Exception as e:
        await message.reply_text(f"<blockquote><b><emoji id=5019523782004441717>❌</emoji> Error: {str(e)}</b></blockquote>")