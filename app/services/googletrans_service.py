import asyncio
from googletrans import Translator

async def translate_word(word: str, target_language: str):
    async with Translator() as translator:
        result = await translator.translate(word, dest=target_language)
        return result.text
