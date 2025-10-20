from PyroUbot import *
import aiohttp
import random
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ғᴀᴍᴇs"
__HELP__ = """
<blockquote><b>🎮 Bantuan Fun Games

⌬ perintah: <code>{0}dice</code>
⊷ Lempar dadu (1-6)

⌬ perintah: <code>{0}coin</code>
⊷ Lempar koin (Heads/Tails)

⌬ perintah: <code>{0}8ball [question]</code>
⊷ Magic 8 Ball - jawab pertanyaan

⌬ perintah: <code>{0}roll [max]</code>
⊷ Roll random number (default 1-100)

⌬ perintah: <code>{0}choose [option1|option2|...]</code>
⊷ Pilih random dari pilihan
⊷ Contoh: <code>{0}choose Nasi|Mie|Roti</code></b></blockquote>
"""

MAGIC_8BALL_RESPONSES = [
    "✅ It is certain",
    "✅ It is decidedly so",
    "✅ Without a doubt",
    "✅ Yes definitely",
    "✅ You may rely on it",
    "✅ As I see it, yes",
    "✅ Most likely",
    "✅ Outlook good",
    "✅ Yes",
    "✅ Signs point to yes",
    "🤷 Reply hazy, try again",
    "🤷 Ask again later",
    "🤷 Better not tell you now",
    "🤷 Cannot predict now",
    "🤷 Concentrate and ask again",
    "❌ Don't count on it",
    "❌ My reply is no",
    "❌ My sources say no",
    "❌ Outlook not so good",
    "❌ Very doubtful"
]

@PY.UBOT("dice")
@PY.TOP_CMD
async def roll_dice(client, message: Message):
    try:
        dice_result = random.randint(1, 6)
        dice_emoji = "🎲"
        
        result = f"""
<blockquote><b>{dice_emoji} Dice Roll</b></blockquote>

<blockquote><b>🎯 Result:</b> {dice_result}</blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
        await message.reply_text(result)
        
    except Exception as e:
        await message.reply_text(f"<emoji id=5019523782004441717>❌</emoji> Error: {str(e)}")

@PY.UBOT("coin|coinflip")
@PY.TOP_CMD
async def flip_coin(client, message: Message):
    try:
        result = random.choice(["Heads 🪙", "Tails 💰"])
        
        text = f"""
<blockquote><b>🪙 Coin Flip</b></blockquote>

<blockquote><b>🎯 Result:</b> {result}</blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
        await message.reply_text(text)
        
    except Exception as e:
        await message.reply_text(f"<emoji id=5019523782004441717>❌</emoji> Error: {str(e)}")

@PY.UBOT("8ball")
@PY.TOP_CMD
async def magic_8ball(client, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji> Ask a question!\nContoh: <code>.8ball Will I be rich?</code>"
            )
            return
        
        question = " ".join(message.command[1:])
        answer = random.choice(MAGIC_8BALL_RESPONSES)
        
        result = f"""
<blockquote><b>🔮 Magic 8-Ball</b></blockquote>

<blockquote><b>❓ Question:</b> {question}
<b>🔮 Answer:</b> {answer}</blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
        await message.reply_text(result)
        
    except Exception as e:
        await message.reply_text(f"<emoji id=5019523782004441717>❌</emoji> Error: {str(e)}")

@PY.UBOT("roll")
@PY.TOP_CMD
async def roll_number(client, message: Message):
    try:
        max_num = 100
        if len(message.command) > 1:
            try:
                max_num = int(message.command[1])
            except:
                pass
        
        result = random.randint(1, max_num)
        
        text = f"""
<blockquote><b>🎲 Number Roll</b></blockquote>

<blockquote><b>🎯 Range:</b> 1-{max_num}
<b>🎯 Result:</b> {result}</blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
        await message.reply_text(text)
        
    except Exception as e:
        await message.reply_text(f"<emoji id=5019523782004441717>❌</emoji> Error: {str(e)}")

@PY.UBOT("choose|pick")
@PY.TOP_CMD
async def choose_option(client, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji> Mohon gunakan format:\n<code>.choose option1|option2|option3</code>"
            )
            return
        
        text = " ".join(message.command[1:])
        options = [opt.strip() for opt in text.split("|")]
        
        if len(options) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji> Minimal 2 pilihan!\nPisahkan dengan |\nContoh: <code>.choose Nasi|Mie|Roti</code>"
            )
            return
        
        chosen = random.choice(options)
        
        result = f"""
<blockquote><b>🎯 Random Choice</b></blockquote>

<blockquote><b>📝 Options:</b>
""" + "\n".join([f"• {opt}" for opt in options]) + f"""

<b>✅ Chosen:</b> {chosen}</blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
        await message.reply_text(result)
        
    except Exception as e:
        await message.reply_text(f"<emoji id=5019523782004441717>❌</emoji> Error: {str(e)}")

@PY.BOT("dice")
async def roll_dice_bot(client, message: Message):
    try:
        dice_result = random.randint(1, 6)
        dice_emoji = "🎲"
        
        result = f"""
<blockquote><b>{dice_emoji} Dice Roll</b></blockquote>

<blockquote><b>🎯 Result:</b> {dice_result}</blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
        await message.reply_text(result)
        
    except Exception as e:
        await message.reply_text(f"<blockquote><b><emoji id=5019523782004441717>❌</emoji> Error: {str(e)}</b></blockquote>")

@PY.BOT("coin|coinflip")
async def flip_coin_bot(client, message: Message):
    try:
        result = random.choice(["Heads 🪙", "Tails 💰"])
        
        text = f"""
<blockquote><b>🪙 Coin Flip</b></blockquote>

<blockquote><b>🎯 Result:</b> {result}</blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
        await message.reply_text(text)
        
    except Exception as e:
        await message.reply_text(f"<blockquote><b><emoji id=5019523782004441717>❌</emoji> Error: {str(e)}</b></blockquote>")