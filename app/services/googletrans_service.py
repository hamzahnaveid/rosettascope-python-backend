import asyncio
from googletrans import Translator

#language hard-coded to Spanish for test/demo purposes
async def translate_word(word: str, target_language: str = "es"):
    async with Translator() as translator:
        result = await translator.translate(word, dest=target_language)
        return result.text
