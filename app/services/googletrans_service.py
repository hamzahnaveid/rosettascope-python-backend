import asyncio
from googletrans import Translator

language_codes = {
    'de-DE': 'de',
    'fr-FR': 'fr',
    'es-ES': 'es',
    'vi-VN': 'vi',
    'zh-CN': 'zh-cn',
    'ar-SA': 'ar',
    'hi-HI': 'hi',
    'ko-KR': 'ko',
    'ja-JP': 'ja',
    'ru-RU': 'ru',
    'sv-SE': 'sv',
    'fi-FI': 'fi',
    'pl-PL': 'pl',
    'it-IT': 'it',
    'nl-NL': 'nl'
}

async def translate_word(word: str, target_language: str):
    async with Translator() as translator:
        language = language_codes[target_language]
        result = await translator.translate(word, dest=language)
        return result.text

async def translate_to_english(word: str, source_language: str):
    async with Translator() as translator:
        language = language_codes[source_language]
        result = await translator.translate(word, dest="en", src=language)
        return result.text
