
import os
from googletrans import Translator


def translate_text(text, source_language, target_language):
    translator = Translator()
    result = translator.translate(text, src=source_language, dest=target_language)
    return result.text


def main():
    print("Text-Based Language Translator")
    print("-------------------------------")

    text = input("Enter the text to translate: ")
    source_language = input("Enter the source language (e.g. en, es, fr): ")
    target_language = input("Enter the target language (e.g. en, es, fr,ar): ")

    translated_text = translate_text(text, source_language, target_language)

    print(f"Translated text: {translated_text}")


if __name__ == "__main__":
    main()