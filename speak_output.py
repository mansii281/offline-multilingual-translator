from TTS.api import TTS

tts = TTS(model_name="tts_models/en/vctk/vits")

with open("translated.txt", "r", encoding="utf-8") as f:
    text = f.read()

tts.tts_to_file(
    text=text,
    speaker="p225",
    file_path="translated.wav"
)
