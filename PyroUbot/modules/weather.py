from PyroUbot import *
import aiohttp
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ᴡᴇᴀᴛʜᴇʀ"
__HELP__ = """
<blockquote><b>🌤️ Bantuan Weather Info

⌬ perintah: <code>{0}weather [kota]</code>
⊷ Cek cuaca real-time di kota manapun
⊷ Contoh: <code>{0}weather Jakarta</code></b></blockquote>
"""

@PY.UBOT("weather|cuaca")
@PY.TOP_CMD
async def weather_info(client, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji> Mohon gunakan format:\n<code>.weather [KOTA]</code>\n\nContoh: <code>.weather Jakarta</code>"
            )
            return
        
        city = " ".join(message.command[1:])
        prs = await message.reply_text(f"<emoji id=6226405134004389590>🔍</emoji> Mengecek cuaca di {city}...")
        
        async with aiohttp.ClientSession() as session:
            # Using wttr.in API (no key required)
            url = f"https://wttr.in/{city}?format=j1"
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    
                    current = data['current_condition'][0]
                    location = data['nearest_area'][0]
                    
                    temp_c = current['temp_C']
                    temp_f = current['temp_F']
                    feels_like = current['FeelsLikeC']
                    humidity = current['humidity']
                    wind_speed = current['windspeedKmph']
                    weather_desc = current['weatherDesc'][0]['value']
                    
                    area_name = location['areaName'][0]['value']
                    country = location['country'][0]['value']
                    
                    # Weather emoji
                    weather_emoji = "☀️"
                    if "cloud" in weather_desc.lower():
                        weather_emoji = "☁️"
                    elif "rain" in weather_desc.lower():
                        weather_emoji = "🌧️"
                    elif "storm" in weather_desc.lower():
                        weather_emoji = "⛈️"
                    elif "snow" in weather_desc.lower():
                        weather_emoji = "🌨️"
                    
                    text = f"""
<blockquote><b>{weather_emoji} Cuaca: {area_name}, {country}</b></blockquote>

<blockquote><b>🌡️ Temperature:</b> {temp_c}°C / {temp_f}°F
<b>🤔 Feels Like:</b> {feels_like}°C
<b>☁️ Kondisi:</b> {weather_desc}
<b>💧 Humidity:</b> {humidity}%
<b>💨 Wind Speed:</b> {wind_speed} km/h</blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
                    await prs.edit(text)
                    return
        
        await prs.edit(f"<emoji id=5019523782004441717>❌</emoji> Kota {city} tidak ditemukan!")
        
    except Exception as e:
        await message.reply_text(f"<emoji id=5019523782004441717>❌</emoji> Error: {str(e)}")

@PY.BOT("weather|cuaca")
async def weather_info_bot(client, message: Message):
    try:
        if len(message.command) < 2:
            await message.reply_text(
                "<blockquote><b><emoji id=5019523782004441717>❌</emoji> Mohon gunakan format:\n<code>/weather [KOTA]</code>\n\nContoh: <code>/weather Jakarta</code></b></blockquote>"
            )
            return
        
        city = " ".join(message.command[1:])
        prs = await message.reply_text(f"<blockquote><b><emoji id=6226405134004389590>🔍</emoji> Mengecek cuaca di {city}...</b></blockquote>")
        
        async with aiohttp.ClientSession() as session:
            url = f"https://wttr.in/{city}?format=j1"
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    
                    current = data['current_condition'][0]
                    location = data['nearest_area'][0]
                    
                    temp_c = current['temp_C']
                    temp_f = current['temp_F']
                    feels_like = current['FeelsLikeC']
                    humidity = current['humidity']
                    wind_speed = current['windspeedKmph']
                    weather_desc = current['weatherDesc'][0]['value']
                    
                    area_name = location['areaName'][0]['value']
                    country = location['country'][0]['value']
                    
                    weather_emoji = "☀️"
                    if "cloud" in weather_desc.lower():
                        weather_emoji = "☁️"
                    elif "rain" in weather_desc.lower():
                        weather_emoji = "🌧️"
                    elif "storm" in weather_desc.lower():
                        weather_emoji = "⛈️"
                    elif "snow" in weather_desc.lower():
                        weather_emoji = "🌨️"
                    
                    text = f"""
<blockquote><b>{weather_emoji} Cuaca: {area_name}, {country}</b></blockquote>

<blockquote><b>🌡️ Temperature:</b> {temp_c}°C / {temp_f}°F
<b>🤔 Feels Like:</b> {feels_like}°C
<b>☁️ Kondisi:</b> {weather_desc}
<b>💧 Humidity:</b> {humidity}%
<b>💨 Wind Speed:</b> {wind_speed} km/h</blockquote>

<blockquote><b>ᣃ࿈ ᴜsᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ ࿈ᣄ</b></blockquote>
"""
                    await prs.edit(text)
                    return
        
        await prs.edit(f"<blockquote><b><emoji id=5019523782004441717>❌</emoji> Kota {city} tidak ditemukan!</b></blockquote>")
        
    except Exception as e:
        await message.reply_text(f"<blockquote><b><emoji id=5019523782004441717>❌</emoji> Error: {str(e)}</b></blockquote>")