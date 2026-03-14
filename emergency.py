from transformers import pipeline

print("Loading translation model...")

translator = pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M"
)

print("Model ready\n")


# Emergency phrases (shown first)
phrases = [
    "I need medical help",
    "Call an ambulance",
    "Where is the nearest shelter",
    "I am injured",
    "I am lost",
    "I need food and water"
]

print("Emergency phrases:\n")

for i, phrase in enumerate(phrases, 1):
    print(i, ".", phrase)


# Language selection
print("\nSelect language for translation:\n")

languages = {
    "1": ("hin_Deva","Hindi"),
    "2": ("spa_Latn","Spanish"),
    "3": ("arb_Arab","Arabic"),
    "4": ("fra_Latn","French"),
    "5": ("deu_Latn","German"),
    "6": ("ita_Latn","Italian"),
    "7": ("zho_Hans","Chinese"),
    "8": ("jpn_Jpan","Japanese"),
    "9": ("kor_Hang","Korean")
}

for k,v in languages.items():
    print(k, v[1])

choice = input("\nEnter number: ")

target = languages.get(choice)

print("\nTranslated emergency phrases:\n")


for phrase in phrases:

    translated = translator(
        phrase,
        src_lang="eng_Latn",
        tgt_lang=target[0]
    )

    output = translated[0]["translation_text"]

    print(output)