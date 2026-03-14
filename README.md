# 🌍 LinguaLock – AI Powered Offline Multilingual Translator

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow?logo=huggingface)
![PyTorch](https://img.shields.io/badge/PyTorch-DeepLearning-red?logo=pytorch)
![OpenCV](https://img.shields.io/badge/OpenCV-ComputerVision-green?logo=opencv)
![OCR](https://img.shields.io/badge/OCR-Tesseract-blue)
![Offline](https://img.shields.io/badge/Mode-Offline-important)
![License](https://img.shields.io/badge/License-MIT-green)

LinguaLock is an **AI-powered multilingual translator that works completely offline**, enabling seamless communication across languages using **text, speech, and images**.

Most translation tools rely on **cloud-based APIs and constant internet connectivity**, which limits their usability in many real-world scenarios. LinguaLock addresses this challenge by running **state-of-the-art AI models locally**, allowing translation capabilities even in **low-connectivity environments, rural areas, disaster zones, and remote travel situations**.

By integrating **natural language processing, speech recognition, and computer vision**, LinguaLock creates a unified system capable of handling multiple forms of communication.

---

# 🚀 Features

## 📝 Text Translation

The text translation module allows users to translate written text between multiple languages using a multilingual transformer model.

The system uses **Meta’s NLLB (No Language Left Behind) model**, designed to support a wide range of languages with strong translation performance. When a user inputs text, it is tokenized and processed by the translation model to generate the translated output in the target language.

This feature enables users to:

* Translate written communication instantly
* Understand foreign-language documents
* Convert typed messages into another language

Since the model runs locally, translations are **fast, private, and independent of internet connectivity**.

---

## 🎤 Speech Translation

The speech translation module allows users to **speak naturally into a microphone and receive translated output**.

The system first captures the audio input and processes it through a speech recognition model (**Whisper**). The spoken language is converted into text, which is then passed into the translation model to generate the translated output.

Pipeline:

Speech Input → Speech Recognition → Text Translation → Output Text

This feature is especially useful for:

* Real-time communication
* Language assistance while traveling
* Hands-free interaction

Because all processing occurs locally, speech translation can operate **even in environments without network access**.

---

## 📷 Image Translation

The image translation module enables the system to **extract text from images and translate it into another language**.

Using **Optical Character Recognition (OCR)**, the system detects and extracts textual content from images such as:

* Street signs
* Restaurant menus
* Printed documents
* Instruction manuals
* Posters or notices

Once the text is extracted using the OCR engine (**Tesseract**), it is sent to the translation model, which produces the translated output.

Pipeline:

Image → OCR Text Extraction → Translation Model → Translated Text

This feature allows users to quickly understand foreign-language information captured through images.

---

## 🌐 Fully Offline Operation

A key design principle of LinguaLock is **complete offline functionality**.

Most translation systems depend on external APIs or cloud-based inference. In contrast, LinguaLock downloads and stores AI models locally, allowing all processing to occur directly on the device.

Benefits include:

* Works without internet connectivity
* Faster processing without network latency
* Increased reliability in remote environments
* Improved privacy since data never leaves the device

This makes the system suitable for **travelers, rural communities, field operations, and emergency response teams**.

---

## ⚡ Edge AI Ready

LinguaLock is designed with **edge computing principles**, meaning the system can run efficiently on local hardware rather than requiring powerful cloud infrastructure.

The architecture supports deployment on:

* Personal computers
* Edge devices
* Local servers
* Portable field systems

Future optimizations such as **model quantization and ONNX conversion** can further improve performance and enable deployment on resource-constrained devices.

---

# 🧠 AI Models Used

| Feature            | Model                            |
| ------------------ | -------------------------------- |
| Text Translation   | facebook/nllb-200-distilled-600M |
| Speech Recognition | Whisper                          |
| Image OCR          | Tesseract OCR                    |

---

# 🛠 Tech Stack

Python • PyTorch • HuggingFace Transformers • OpenCV • Tesseract OCR • SpeechRecognition • NumPy

These technologies combine **machine learning, natural language processing, speech processing, and computer vision** into a unified application pipeline.

---

# ⚙️ How It Works

LinguaLock follows a **modular AI pipeline** where each input type is processed independently before passing through a shared translation engine.

### Text Translation Pipeline

Text Input → Tokenization → NLLB Translation Model → Translated Output

### Speech Translation Pipeline

Speech Input → Whisper Speech Recognition → Text Translation Model → Translated Output

### Image Translation Pipeline

Image Input → OCR Text Extraction (Tesseract) → Translation Model → Translated Output

All pipelines converge into the same **translation engine**, ensuring consistency across outputs.

---

# 📊 System Architecture

Input (Text / Speech / Image) → Preprocessing → AI Models (Whisper / NLLB / OCR) → Translation Engine → Translated Output (Text / Speech)

---

# 🌍 Use Cases

• Travelers communicating in foreign countries
• Rural communities with limited internet connectivity
• Disaster response communication
• Cross-language education
• International collaboration without connectivity barriers

---

# 🔮 Future Improvements

* Real-time multilingual conversation mode
* Mobile application deployment
* Edge optimization with ONNX / TensorRT
* Support for additional languages
* Sign language translation integration

---

# ⭐ Support

If you found this project useful, please consider **starring the repository**.

