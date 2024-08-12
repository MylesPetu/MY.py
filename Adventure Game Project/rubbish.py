"""
import re

txt = "Today is a good day and it is Friday"
x = re.search("good.*and", txt)
print(x)
if x:
    print("We have found a match")
else:
    print("we don't have a match")
"""
from googletrans import Translator, LANGUAGES

def translate_text(text, source_language, target_language):
    translator = Translator()
    try:
        result = translator.translate(text, src=source_language, dest=target_language)
        return result.text
    except Exception as e:
        return f"An error occurred during translation: {e}"

def main():
    print("Text-Based Language Translator")
    print("-------------------------------")

    text = input("Enter the text to translate: ")

    print("\nSupported Languages:")
    for code, name in LANGUAGES.items():
        print(f"{code}: {name}")

    source_language = input("\nEnter the source language code (e.g. en, es, fr): ").lower()
    if source_language not in LANGUAGES:
        print("Invalid source language code. Please enter a valid language code.")
        return

    target_language = input("Enter the target language code (e.g. en, es, fr): ").lower()
    if target_language not in LANGUAGES:
        print("Invalid target language code. Please enter a valid language code.")
        return

    translated_text = translate_text(text, source_language, target_language)
    print(f"\nTranslated text: {translated_text}")

if __name__ == "__main__":
    main()