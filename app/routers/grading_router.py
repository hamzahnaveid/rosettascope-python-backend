import json
from fastapi import APIRouter
from app.services.pronunciation_assessment_service import pronunciation_assessment
from app.services.base64_to_wav_service import base64_to_wav
from app.services.ollama_service import generate_feedback
from app.services.bkt_service import calculate_confidence_mastered
from app.schemas.grading_schema import GradingRequest, GradingResponse

router = APIRouter()

@router.post("/grade", response_model=GradingResponse)
async def grade_speech(req: GradingRequest):
    base64_to_wav(req.recordingAudioBytes)

    result = pronunciation_assessment(req.refText, req.targetLanguage)
    feedback = generate_feedback(result)

    oResult = json.loads(result)
    pronScore = oResult['NBest'][0]['PronunciationAssessment']['PronScore']
    isCorrect: bool = False
    if (pronScore >= 90):
        isCorrect = True
    new_confidence_mastered = calculate_confidence_mastered(req.confidenceMastered, isCorrect)
    return {
        "result": result,
        "feedback": feedback,
        "new_confidence_mastered": new_confidence_mastered
    }       