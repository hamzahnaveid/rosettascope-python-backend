from typing import Annotated
from fastapi import APIRouter, Query
from app.services.ollama_service import generate_challenge_hints
from app.services.bkt_service import calculate_challenge_confidence_mastered
from app.services.speech_sdk_service import synthesize_speech
from app.services.pronunciation_assessment_service import pronunciation_assessment

router = APIRouter()

@router.get("/scavenger-hunt", response_model=str)
async def get_hints(words: Annotated[list[str] | None, Query()] = None):
    hints = generate_challenge_hints(words)
    return hints

@router.get("/update-bkt-score-challenge/{confidence_mastered}/{isCorrect}", response_model=float)
async def get_confidence_mastered(confidence_mastered: str, isCorrect: str):
    confidence_mastered = float(confidence_mastered)

    if (isCorrect == 'true'):
        isCorrect = True 
    else : 
        isCorrect = False

    new_confidence_mastered = calculate_challenge_confidence_mastered(confidence_mastered, isCorrect)
    return new_confidence_mastered

@router.get("/get-audio-base64/{text}/{target_language}", response_model=str)
async def get_pronun_audio(text: str, target_language: str):
    return synthesize_speech(text, target_language)