import cv2
import pytesseract
from transformers import pipeline
from langdetect import detect

print("Loading translation model...")

translator = pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M"
)

print("Model ready\n")

# language menu
lang_menu = {
    "1": ("hin_Deva","Hindi"),
    "2": ("spa_Latn","Spanish"),
    "3": ("arb_Arab","Arabic"),
    "4": ("fra_Latn","French"),
    "5": ("deu_Latn","German"),
    "6": ("ita_Latn","Italian"),
    "7": ("zho_Hans","Chinese"),
    "8": ("jpn_Jpan","Japanese"),
    "9": ("kor_Hang","Korean"),
    "10": ("eng_Latn","English")
}

print("Opening camera... Press SPACE to capture")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)

    if key == 32:  # SPACE key
        image = frame
        break

cap.release()
cv2.destroyAllWindows()

print("\nExtracting text from image...")

text = pytesseract.image_to_string(image)

if text.strip() == "":
    print("No text detected")
    exit()

print("\nDetected text:")
print(text)

# Detect source language automatically
try:
    detected = detect(text)
except:
    detected = "en"

print("\nDetected language:", detected)

print("\nSelect language to translate into")

for k,v in lang_menu.items():
    print(k,v[1])

choice = input("Enter number: ")
target = lang_menu[choice]

# Map detected language to NLLB codes
lang_map = {
    "en": "eng_Latn",
    "hi": "hin_Deva",
    "es": "spa_Latn",
    "ar": "arb_Arab",
    "fr": "fra_Latn",
    "de": "deu_Latn",
    "it": "ita_Latn",
    "zh": "zho_Hans",
    "ja": "jpn_Jpan",
    "ko": "kor_Hang"
}

src_lang = lang_map.get(detected, "eng_Latn")

print("\nTranslating...")

translated = translator(
    text,
    src_lang=src_lang,
    tgt_lang=target[0]
)

output = translated[0]["translation_text"]

print("\nTranslated (" + target[1] + "):")
print(output)