from PyroUbot import *
import aiohttp
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ᴜʀʟꜱʜᴏʀᴛ"
__HELP__ = """
<blockquote><b>🔗 Bantuan URL Shortener

⌬ perintah: <code>{0}short [url]</code>
⊷ Perpendek URL panjang menjadi pendek
⊷ Contoh: <code>{0}short https://example.com/very/long/url</code></b></blockquote>
"""

@PY.UBOT("short|shorturl")
@PY.TOP_CMD
async def url_shortener(client, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji> Mohon gunakan format:\n<code>.short [URL]</code>\n\nContoh: <code>.short https://example.com</code>"
            )
            return
        
        url = message.command[1]
        prs = await message.reply_text(f"<emoji id=6226405134004389590>🔍</emoji> Mempersingkat URL...")
        
        async with aiohttp.ClientSession() as session:
            # Using TinyURL API
            api_url = f"https://tinyurl.com/api-create.php?url={url}"
            async with session.get(api_url) as resp:
                if resp.status == 200:
                    short_url = await resp.text()
                    
                    text = f"""
<blockquote><b>🔗 URL Shortened!</b></blockquote>

<blockquote><b>🔗 Original:</b> {url[:50]}{'...' if len(url) > 50 else ''}
<b>✅ Short URL:</b> {short_url}</blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
                    await prs.edit(text)
                    return
        
        await prs.edit(f"<emoji id=5019523782004441717>❌</emoji> Gagal mempersingkat URL!")
        
    except Exception as e:
        await message.reply_text(f"<emoji id=5019523782004441717>❌</emoji> Error: {str(e)}")

@PY.BOT("short|shorturl")
async def url_shortener_bot(client, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text(
                "<blockquote><b><emoji id=5019523782004441717>❌</emoji> Mohon gunakan format:\n<code>/short [URL]</code>\n\nContoh: <code>/short https://example.com</code></b></blockquote>"
            )
            return
        
        url = message.command[1]
        prs = await message.reply_text(f"<blockquote><b><emoji id=6226405134004389590>🔍</emoji> Mempersingkat URL...</b></blockquote>")
        
        async with aiohttp.ClientSession() as session:
            api_url = f"https://tinyurl.com/api-create.php?url={url}"
            async with session.get(api_url) as resp:
                if resp.status == 200:
                    short_url = await resp.text()
                    
                    text = f"""
<blockquote><b>🔗 URL Shortened!</b></blockquote>

<blockquote><b>🔗 Original:</b> {url[:50]}{'...' if len(url) > 50 else ''}
<b>✅ Short URL:</b> {short_url}</blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
                    await prs.edit(text)
                    return
        
        await prs.edit(f"<blockquote><b><emoji id=5019523782004441717>❌</emoji> Gagal mempersingkat URL!</b></blockquote>")
        
    except Exception as e:
        await message.reply_text(f"<blockquote><b><emoji id=5019523782004441717>❌</emoji> Error: {str(e)}</b></blockquote>")