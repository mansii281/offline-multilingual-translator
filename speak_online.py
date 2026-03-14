import asyncio
import edge_tts
import os

text = open("translated.txt","r",encoding="utf-8").read().strip()
lang = open("lang.txt","r").read().strip()

voices = {
    "Hindi": "hi-IN-SwaraNeural",
    "German": "de-DE-KatjaNeural",
    "English": "en-US-AriaNeural",
    "Spanish": "es-ES-ElviraNeural",
    "French": "fr-FR-DeniseNeural",
    "Italian": "it-IT-ElsaNeural",
    "Japanese": "ja-JP-NanamiNeural",
    "Chinese": "zh-CN-XiaoxiaoNeural",
    "Korean": "ko-KR-SunHiNeural",
    "Arabic": "ar-SA-ZariyahNeural"
}

voice = voices.get(lang,"en-US-AriaNeural")

async def speak():

    communicate = edge_tts.Communicate(text,voice)

    await communicate.save("translated.mp3")

asyncio.run(speak())

os.system("afplay translated.mp3")