from faster_whisper import WhisperModel

model = WhisperModel("small")

segments, info = model.transcribe("test.wav")

for segment in segments:
    print(segment.text)
