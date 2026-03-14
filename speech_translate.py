import os
import socket
from faster_whisper import WhisperModel
from transformers import pipeline

print("Loading models...")

speech_model = WhisperModel(
    "medium",
    compute_type="int8",
    cpu_threads=4
)

translator = pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M"
)

print("Models ready\n")


def is_online():
    try:
        socket.create_connection(("8.8.8.8",53),2)
        return True
    except:
        return False


languages = {
    "1": ("hin_Deva","Hindi","hi"),
    "2": ("spa_Latn","Spanish","es"),
    "3": ("arb_Arab","Arabic","ar"),
    "4": ("fra_Latn","French","fr"),
    "5": ("deu_Latn","German","de"),
    "6": ("ita_Latn","Italian","it"),
    "7": ("zho_Hans","Chinese","zh"),
    "8": ("jpn_Jpan","Japanese","ja"),
    "9": ("kor_Hang","Korean","ko"),
    "10": ("eng_Latn","English","en")
}


print("Select source language\n")

for k,v in languages.items():
    print(k,v[1])

choice = input("Enter number: ")
src = languages.get(choice)


print("\nSelect language to translate into\n")

for k,v in languages.items():
    print(k,v[1])

choice = input("Enter number: ")
tgt = languages.get(choice)
print("\nStart speaking when prompted...\n")

os.system("python3 recorder.py")


segments, info = speech_model.transcribe(
    "test.wav",
    language=src[2],
    task="transcribe",
    beam_size=3
)


spoken = "".join([s.text for s in segments]).strip()


if spoken == "":
    print("No speech detected. Please try again.")
    exit()


# Fix common Whisper mistakes
corrections = {

    "Namaste": "नमस्ते",
    "Myra": "मेरा",
    "Namaansi": "नाम मानसी",
    "Namaansi hai": "नाम मानसी है",

    "میرا": "मेरा",
    "نام": "नाम",
    "مانسی": "मानसी",
    "ہے": "है",

    "Panty": "Mansi",
    "Mancy": "Mansi",
    "Manty": "Mansi"
}


for wrong, correct in corrections.items():
    spoken = spoken.replace(wrong, correct)


print("\nYou said:", spoken)


try:

    translated = translator(
        spoken,
        src_lang=src[0],
        tgt_lang=tgt[0]
    )

    output = translated[0]["translation_text"]

except Exception as e:

    print("Translation error:", e)
    exit()


print("\nTranslated ("+tgt[1]+"):")
print(output)


with open("translated.txt","w",encoding="utf-8") as f:
    f.write(output)


with open("lang.txt","w") as f:
    f.write(tgt[1])


if is_online():
    os.system("python3 speak_online.py")
else:
    print("\nOffline mode → text only")