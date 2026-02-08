from fastapi import APIRouter
from app.services.googletrans_service import translate_word, translate_to_english
from app.services.ollama_service import generate_phrase
from app.services.speech_sdk_service import synthesize_speech
from app.schemas.translation_schema import TranslationRequest, TranslationResponse

router = APIRouter()

@router.post("/translate", response_model=TranslationResponse)
async def translate_and_speak(req: TranslationRequest):
    translated_word = await translate_word(req.word, req.targetLanguage)

    #used when user learning level is sufficient - added as parameter in synthesize_speech instead of var translated_word
    ollama_response = generate_phrase(translated_word, req.targetLanguage)
    generated_phrase = ollama_response.get("response")
    
    original_text = await translate_to_english(generated_phrase, req.targetLanguage)

    pronunciation_audio_base64 = synthesize_speech(generated_phrase, req.targetLanguage)
    return {
        "translation": generated_phrase,
        "translated_word": translated_word,
        "original_text": original_text,
        "pronunciation_audio_base64": pronunciation_audio_base64
        }

@router.get("/translate-word/{word}/{srcLanguage}", response_model=str)
async def translate_word_to_english(word: str, srcLanguage: str):
    translated_word = await translate_to_english(word, srcLanguage)
    return translated_word
