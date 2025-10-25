from fastapi import APIRouter
from app.services.googletrans_service import translate_word
from app.services.speech_sdk_service import synthesize_speech
from app.schemas.translation_schema import TranslationRequest, TranslationResponse

router = APIRouter()

@router.post("/translate", response_model=TranslationResponse)
async def translate_and_speak(req: TranslationRequest):
    #language hard-coded to Spanish for test/demo purposes
    translated_word = await translate_word(req.word)
    pronunciation_audio_base64 = synthesize_speech(translated_word)
    return {
        "translated_word": translated_word,
        "pronunciation_audio_base64": pronunciation_audio_base64
        }