from PyroUbot import *
import aiohttp
import io
from pyrogram import filters
from pyrogram.types import Message
import base64

__MODULE__ = "ᴄᴏɴᴠᴇʀᴛ"
__HELP__ = """
<blockquote><b>🔄 Bantuan Text Converter

⌬ perintah: <code>{0}base64 encode [text]</code>
⊷ Encode text ke Base64

⌬ perintah: <code>{0}base64 decode [text]</code>
⊷ Decode Base64 ke text

⌬ perintah: <code>{0}binary [text]</code>
⊷ Convert text ke binary

⌬ perintah: <code>{0}hex [text]</code>
⊷ Convert text ke hexadecimal

⌬ perintah: <code>{0}reverse [text]</code>
⊷ Reverse text</b></blockquote>
"""

@PY.UBOT("base64")
@PY.TOP_CMD
async def base64_convert(client, message: Message):
    try:
        if len(message.command) < 3:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji> Mohon gunakan format:\n<code>.base64 [encode/decode] [text]</code>"
            )
            return
        
        action = message.command[1].lower()
        text = " ".join(message.command[2:])
        
        if action == "encode":
            encoded = base64.b64encode(text.encode()).decode()
            result = f"""
<blockquote><b>🔒 Base64 Encoded</b></blockquote>

<blockquote><b>📝 Original:</b> {text}
<b>🔐 Encoded:</b> <code>{encoded}</code></blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
            await message.reply_text(result)
        
        elif action == "decode":
            try:
                decoded = base64.b64decode(text.encode()).decode()
                result = f"""
<blockquote><b>🔓 Base64 Decoded</b></blockquote>

<blockquote><b>🔐 Encoded:</b> {text}
<b>📝 Decoded:</b> <code>{decoded}</code></blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
                await message.reply_text(result)
            except:
                await message.reply_text("<emoji id=5019523782004441717>❌</emoji> Invalid Base64 string!")
        else:
            await message.reply_text("<emoji id=5019523782004441717>❌</emoji> Action harus 'encode' atau 'decode'")
        
    except Exception as e:
        await message.reply_text(f"<emoji id=5019523782004441717>❌</emoji> Error: {str(e)}")

@PY.UBOT("binary")
@PY.TOP_CMD
async def binary_convert(client, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji> Mohon gunakan format:\n<code>.binary [text]</code>"
            )
            return
        
        text = " ".join(message.command[1:])
        binary = ' '.join(format(ord(c), '08b') for c in text)
        
        result = f"""
<blockquote><b>🔢 Binary Conversion</b></blockquote>

<blockquote><b>📝 Original:</b> {text}
<b>🔢 Binary:</b> <code>{binary}</code></blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
        await message.reply_text(result)
        
    except Exception as e:
        await message.reply_text(f"<emoji id=5019523782004441717>❌</emoji> Error: {str(e)}")

@PY.UBOT("hex|hexcode")
@PY.TOP_CMD
async def hex_convert(client, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji> Mohon gunakan format:\n<code>.hex [text]</code>"
            )
            return
        
        text = " ".join(message.command[1:])
        hexcode = text.encode().hex()
        
        result = f"""
<blockquote><b>🔢 Hexadecimal Conversion</b></blockquote>

<blockquote><b>📝 Original:</b> {text}
<b>🔢 Hex:</b> <code>{hexcode}</code></blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
        await message.reply_text(result)
        
    except Exception as e:
        await message.reply_text(f"<emoji id=5019523782004441717>❌</emoji> Error: {str(e)}")

@PY.UBOT("reverse")
@PY.TOP_CMD
async def reverse_text(client, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji> Mohon gunakan format:\n<code>.reverse [text]</code>"
            )
            return
        
        text = " ".join(message.command[1:])
        reversed_text = text[::-1]
        
        result = f"""
<blockquote><b>🔄 Text Reversed</b></blockquote>

<blockquote><b>📝 Original:</b> {text}
<b>🔄 Reversed:</b> <code>{reversed_text}</code></blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
        await message.reply_text(result)
        
    except Exception as e:
        await message.reply_text(f"<emoji id=5019523782004441717>❌</emoji> Error: {str(e)}")

@PY.BOT("base64")
async def base64_convert_bot(client, message: Message):
    try:
        if len(message.command) < 3:
            await message.reply_text(
                "<blockquote><b><emoji id=5019523782004441717>❌</emoji> Mohon gunakan format:\n<code>/base64 [encode/decode] [text]</code></b></blockquote>"
            )
            return
        
        action = message.command[1].lower()
        text = " ".join(message.command[2:])
        
        if action == "encode":
            encoded = base64.b64encode(text.encode()).decode()
            result = f"""
<blockquote><b>🔒 Base64 Encoded</b></blockquote>

<blockquote><b>📝 Original:</b> {text}
<b>🔐 Encoded:</b> <code>{encoded}</code></blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
            await message.reply_text(result)
        
        elif action == "decode":
            try:
                decoded = base64.b64decode(text.encode()).decode()
                result = f"""
<blockquote><b>🔓 Base64 Decoded</b></blockquote>

<blockquote><b>🔐 Encoded:</b> {text}
<b>📝 Decoded:</b> <code>{decoded}</code></blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
                await message.reply_text(result)
            except:
                await message.reply_text("<blockquote><b><emoji id=5019523782004441717>❌</emoji> Invalid Base64 string!</b></blockquote>")
        
    except Exception as e:
        await message.reply_text(f"<blockquote><b><emoji id=5019523782004441717>❌</emoji> Error: {str(e)}</b></blockquote>")