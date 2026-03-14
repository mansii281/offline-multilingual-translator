import sounddevice as sd
import soundfile as sf
import numpy as np

fs = 16000
recording = []

print("Press ENTER to start recording")
input()

print("Recording... Speak now")
print("Press ENTER to stop recording")

def callback(indata, frames, time, status):
    recording.append(indata.copy())

with sd.InputStream(samplerate=fs, channels=1, callback=callback):
    input()

if len(recording) == 0:
    print("No audio captured. Please speak after starting recording.")
    exit()
    
audio = np.concatenate(recording, axis=0)

sf.write("test.wav", audio, fs)

print("Recording saved as test.wav")