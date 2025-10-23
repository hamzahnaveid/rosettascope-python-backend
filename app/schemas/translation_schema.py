from pydantic import BaseModel

class TranslationRequest(BaseModel):
    word: str
    targetLanguage: str

class TranslationResponse(BaseModel):
    translated_word: str
    pronunciation_audio_base64: str