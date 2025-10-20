from PyroUbot import *
import aiohttp
import io
from pyrogram import filters
from pyrogram.types import Message
from PIL import Image, ImageDraw, ImageFont
import random

__MODULE__ = "ᴍᴇᴍᴇ"
__HELP__ = """
<blockquote><b>😂 Bantuan Meme Generator

⌬ perintah: <code>{0}meme</code>
⊷ Dapatkan meme random dari internet

⌬ perintah: <code>{0}makememe [top_text] | [bottom_text]</code>
⊷ Buat custom meme (reply ke gambar)
⊷ Contoh: <code>{0}makememe When you code | And it works</code></b></blockquote>
"""

@PY.UBOT("meme")
@PY.TOP_CMD
async def random_meme(client, message: Message):
    try:
        prs = await message.reply_text(f"<emoji id=6226405134004389590>🔍</emoji> Mencari meme lucu...")
        
        async with aiohttp.ClientSession() as session:
            # Using meme API
            api_url = "https://meme-api.com/gimme"
            async with session.get(api_url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    
                    meme_url = data['url']
                    title = data['title']
                    subreddit = data['subreddit']
                    author = data['author']
                    ups = data['ups']
                    
                    # Download and send meme
                    async with session.get(meme_url) as img_resp:
                        if img_resp.status == 200:
                            meme_image = await img_resp.read()
                            
                            caption = f"""
<blockquote><b>😂 {title}</b>

<b>📌 Subreddit:</b> r/{subreddit}
<b>👤 Author:</b> u/{author}
<b>👍 Upvotes:</b> {ups}

<b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
                            
                            await message.reply_photo(
                                photo=io.BytesIO(meme_image),
                                caption=caption
                            )
                            await prs.delete()
                            return
        
        await prs.edit(f"<emoji id=5019523782004441717>❌</emoji> Gagal mendapatkan meme!")
        
    except Exception as e:
        await message.reply_text(f"<emoji id=5019523782004441717>❌</emoji> Error: {str(e)}")

@PY.UBOT("makememe")
@PY.TOP_CMD
async def make_meme(client, message: Message):
    try:
        if not message.reply_to_message or not message.reply_to_message.photo:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji> Reply ke gambar dan gunakan format:\n<code>.makememe TOP TEXT | BOTTOM TEXT</code>"
            )
            return
        
        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji> Mohon masukkan text!\nFormat: <code>.makememe TOP TEXT | BOTTOM TEXT</code>"
            )
            return
        
        prs = await message.reply_text(f"<emoji id=6226405134004389590>🔍</emoji> Membuat meme...")
        
        # Parse text
        text_input = " ".join(message.command[1:])
        if "|" in text_input:
            top_text, bottom_text = text_input.split("|", 1)
            top_text = top_text.strip()
            bottom_text = bottom_text.strip()
        else:
            top_text = text_input
            bottom_text = ""
        
        # Download image
        photo_path = await message.reply_to_message.download()
        
        # Open and process image
        img = Image.open(photo_path)
        draw = ImageDraw.Draw(img)
        
        # Calculate font size based on image size
        width, height = img.size
        font_size = int(height * 0.08)
        
        try:
            font = ImageFont.truetype("/app/storage/default.ttf", font_size)
        except:
            font = ImageFont.load_default()
        
        # Draw top text
        if top_text:
            # Get text bounding box
            bbox = draw.textbbox((0, 0), top_text.upper(), font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            x = (width - text_width) / 2
            y = 20
            
            # Draw text with black outline
            outline_range = 2
            for adj_x in range(-outline_range, outline_range + 1):
                for adj_y in range(-outline_range, outline_range + 1):
                    draw.text((x + adj_x, y + adj_y), top_text.upper(), font=font, fill="black")
            draw.text((x, y), top_text.upper(), font=font, fill="white")
        
        # Draw bottom text
        if bottom_text:
            bbox = draw.textbbox((0, 0), bottom_text.upper(), font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            x = (width - text_width) / 2
            y = height - text_height - 30
            
            # Draw text with black outline
            outline_range = 2
            for adj_x in range(-outline_range, outline_range + 1):
                for adj_y in range(-outline_range, outline_range + 1):
                    draw.text((x + adj_x, y + adj_y), bottom_text.upper(), font=font, fill="black")
            draw.text((x, y), bottom_text.upper(), font=font, fill="white")
        
        # Save to BytesIO
        output = io.BytesIO()
        img.save(output, format='JPEG')
        output.seek(0)
        
        await message.reply_photo(
            photo=output,
            caption="<blockquote><b>😂 Meme Created!\n\nᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>"
        )
        await prs.delete()
        
        # Clean up
        import os
        os.remove(photo_path)
        
    except Exception as e:
        await message.reply_text(f"<emoji id=5019523782004441717>❌</emoji> Error: {str(e)}")

@PY.BOT("meme")
async def random_meme_bot(client, message: Message):
    try:
        prs = await message.reply_text(f"<blockquote><b><emoji id=6226405134004389590>🔍</emoji> Mencari meme lucu...</b></blockquote>")
        
        async with aiohttp.ClientSession() as session:
            api_url = "https://meme-api.com/gimme"
            async with session.get(api_url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    
                    meme_url = data['url']
                    title = data['title']
                    subreddit = data['subreddit']
                    author = data['author']
                    ups = data['ups']
                    
                    async with session.get(meme_url) as img_resp:
                        if img_resp.status == 200:
                            meme_image = await img_resp.read()
                            
                            caption = f"""
<blockquote><b>😂 {title}</b>

<b>📌 Subreddit:</b> r/{subreddit}
<b>👤 Author:</b> u/{author}
<b>👍 Upvotes:</b> {ups}

<b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
                            
                            await message.reply_photo(
                                photo=io.BytesIO(meme_image),
                                caption=caption
                            )
                            await prs.delete()
                            return
        
        await prs.edit(f"<blockquote><b><emoji id=5019523782004441717>❌</emoji> Gagal mendapatkan meme!</b></blockquote>")
        
    except Exception as e:
        await message.reply_text(f"<blockquote><b><emoji id=5019523782004441717>❌</emoji> Error: {str(e)}</b></blockquote>")