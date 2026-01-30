import asyncio
from googletrans import Translator

language_codes = {
    'en-US': 'en',
    'zh-CN': 'zh-cn',
    'de-DE': 'de',
    'fr-FR': 'fr',
    'ko-KR': 'ko',
    'ja-JP': 'ja',
    'ru-RU': 'ru',
    'es-ES': 'es'
}

async def translate_word(word: str, target_language: str):
    async with Translator() as translator:
        language = language_codes[target_language]
        result = await translator.translate(word, dest=language)
        return result.text
