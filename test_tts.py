from TTS.api import TTS

tts = TTS(model_name="tts_models/en/vctk/vits")

tts.tts_to_file(
    text="Offline multilingual system voice is working",
    speaker="p225",
    file_path="output.wav"
)
