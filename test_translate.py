from transformers import pipeline

translator = pipeline("translation", model="facebook/nllb-200-distilled-600M")

result = translator("Hello, how are you?", src_lang="eng_Latn", tgt_lang="hin_Deva")

print(result)
