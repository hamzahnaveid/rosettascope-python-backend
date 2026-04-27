import ast
import json
import re
from fastapi import APIRouter
from app.services.googletrans_service import translate_to_english, translate_word
from app.services.ollama_service import generate_beginner_term, generate_phrase, generate_sentence, generate_fluff
from app.services.speech_sdk_service import synthesize_speech
from app.schemas.training_schema import TrainingRequest, TrainingResponse, TrainingBatchResponse

router = APIRouter()

@router.post("/training", response_model=TrainingBatchResponse)
async def get_training_batch(req: TrainingRequest):
    results = []
    for i in range(len(req.trainingWord)):
        trainingWord = req.trainingWord[i]
        confidence = req.confidenceMastered[i]

        if (confidence > 0.24 and confidence <= 0.76):
            level = "INTERMEDIATE"
        elif (confidence > 0.76) :
            level = "ADVANCED"
        else:
            level = "BEGINNER"

        translation = await translate_word(req.trainingWord[i], req.targetLanguage)

        # generating different text for each area to make exercises more engaging
        if (level == "INTERMEDIATE"):
            ollama_response = generate_phrase(translation, req.targetLanguage)
            speaking_text = ollama_response.get("response")
        elif (level == "ADVANCED"):
            ollama_response = generate_sentence(translation, req.targetLanguage)
            speaking_text = ollama_response.get("response")
        else:
            speaking_text = generate_beginner_term(translation, req.targetLanguage)

        speaking_tts_audio_base64 = synthesize_speech(speaking_text, req.targetLanguage)

        if (level == "INTERMEDIATE"):
            ollama_response = generate_phrase(translation, req.targetLanguage)
            listening_text = ollama_response.get("response")
        elif (level == "ADVANCED"):
            ollama_response = generate_sentence(translation, req.targetLanguage)
            listening_text = ollama_response.get("response")
        else:
            listening_text = generate_beginner_term(translation, req.targetLanguage)

        listening_fluff_words = parse_fluff(generate_fluff(listening_text, req.targetLanguage, level))
        listening_tts_audio_base64 = synthesize_speech(listening_text, req.targetLanguage)

        if (level == "INTERMEDIATE"):
            ollama_response = generate_phrase(translation, req.targetLanguage)
            reading_text = ollama_response.get("response")
        elif (level == "ADVANCED"):
            ollama_response = generate_sentence(translation, req.targetLanguage)
            reading_text = ollama_response.get("response")
        else:
            reading_text = generate_beginner_term(translation, req.targetLanguage)

        reading_answer = await translate_to_english(reading_text, req.targetLanguage)


        trainingData = TrainingResponse(
            word=req.trainingWord[i],
              translation=translation,
              speaking_text=speaking_text,
              speaking_pronunciation_audio_base64=speaking_tts_audio_base64,
              listening_text=listening_text,
              listening_fluff_words=listening_fluff_words,
              listening_pronunciation_audio_base64=listening_tts_audio_base64,
              reading_text=reading_text,
              reading_answer=reading_answer
              )
        results.append(trainingData)
    
    return {
        "results": results
    }

def parse_fluff(response_text):
    match = re.search(r'\[.*?\]', response_text, re.S)

    if not match:
        return []

    try:
        return ast.literal_eval(match.group())
    except Exception:
        return []
    
