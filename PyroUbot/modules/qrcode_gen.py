from PyroUbot import *
import aiohttp
import io
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ǫʀᴄᴏᴅᴇ"
__HELP__ = """
<blockquote><b>📱 Bantuan QR Code Generator

⌬ perintah: <code>{0}qr [text/url]</code>
⊷ Generate QR Code dari text atau URL
⊷ Contoh: <code>{0}qr https://t.me/username</code>

⌬ perintah: <code>{0}qrread</code>
⊷ Baca QR Code dari gambar (reply ke gambar)</b></blockquote>
"""

@PY.UBOT("qr|qrcode")
@PY.TOP_CMD
async def generate_qr(client, message: Message):
    try:
        if len(message.command) < 2 and not message.reply_to_message:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji> Mohon gunakan format:\n<code>.qr [TEXT/URL]</code>\n\nContoh: <code>.qr https://t.me/username</code>"
            )
            return
        
        # Get text from command or replied message
        if message.reply_to_message and message.reply_to_message.text:
            text = message.reply_to_message.text
        else:
            text = " ".join(message.command[1:])
        
        prs = await message.reply_text(f"<emoji id=6226405134004389590>🔍</emoji> Generating QR Code...")
        
        # Use QR Code API
        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=500x500&data={text}"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(qr_url) as resp:
                if resp.status == 200:
                    qr_image = await resp.read()
                    
                    # Send as photo
                    await message.reply_photo(
                        photo=io.BytesIO(qr_image),
                        caption=f"<blockquote><b>📱 QR Code Generated!</b>\n\n<b>Content:</b> {text[:100]}{'...' if len(text) > 100 else ''}\n\n<b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>"
                    )
                    await prs.delete()
                    return
        
        await prs.edit(f"<emoji id=5019523782004441717>❌</emoji> Gagal generate QR Code!")
        
    except Exception as e:
        await message.reply_text(f"<emoji id=5019523782004441717>❌</emoji> Error: {str(e)}")

@PY.UBOT("qrread|scanqr")
@PY.TOP_CMD
async def read_qr(client, message: Message):
    try:
        if not message.reply_to_message or not message.reply_to_message.photo:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji> Reply ke gambar QR Code untuk dibaca!"
            )
            return
        
        prs = await message.reply_text(f"<emoji id=6226405134004389590>🔍</emoji> Reading QR Code...")
        
        # Download the photo
        photo = await message.reply_to_message.download(in_memory=True)
        
        # Use QR Code reading API
        async with aiohttp.ClientSession() as session:
            form = aiohttp.FormData()
            form.add_field('file', photo, filename='qrcode.jpg')
            
            async with session.post('https://api.qrserver.com/v1/read-qr-code/', data=form) as resp:
                if resp.status == 200:
                    result = await resp.json()
                    if result and result[0]['symbol'][0]['data']:
                        qr_data = result[0]['symbol'][0]['data']
                        await prs.edit(
                            f"<blockquote><b>📱 QR Code Content:</b>\n\n{qr_data}\n\n<b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>"
                        )
                        return
        
        await prs.edit(f"<emoji id=5019523782004441717>❌</emoji> Tidak dapat membaca QR Code!")
        
    except Exception as e:
        await message.reply_text(f"<emoji id=5019523782004441717>❌</emoji> Error: {str(e)}")

@PY.BOT("qr|qrcode")
async def generate_qr_bot(client, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text(
                "<blockquote><b><emoji id=5019523782004441717>❌</emoji> Mohon gunakan format:\n<code>/qr [TEXT/URL]</code>\n\nContoh: <code>/qr https://t.me/username</code></b></blockquote>"
            )
            return
        
        text = " ".join(message.command[1:])
        prs = await message.reply_text(f"<blockquote><b><emoji id=6226405134004389590>🔍</emoji> Generating QR Code...</b></blockquote>")
        
        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=500x500&data={text}"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(qr_url) as resp:
                if resp.status == 200:
                    qr_image = await resp.read()
                    
                    await message.reply_photo(
                        photo=io.BytesIO(qr_image),
                        caption=f"<blockquote><b>📱 QR Code Generated!</b>\n\n<b>Content:</b> {text[:100]}{'...' if len(text) > 100 else ''}\n\n<b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>"
                    )
                    await prs.delete()
                    return
        
        await prs.edit(f"<blockquote><b><emoji id=5019523782004441717>❌</emoji> Gagal generate QR Code!</b></blockquote>")
        
    except Exception as e:
        await message.reply_text(f"<blockquote><b><emoji id=5019523782004441717>❌</emoji> Error: {str(e)}</b></blockquote>")