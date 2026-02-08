from pydantic import BaseModel

class TranslationRequest(BaseModel):
    word: str
    targetLanguage: str

class TranslationResponse(BaseModel):
    translation: str
    translated_word: str
    original_text: str
    pronunciation_audio_base64: str