from fastapi import APIRouter
from app.services.pronunciation_assessment_service import pronunciation_assessment
from app.services.base64_to_wav_service import base64_to_wav
from app.schemas.grading_schema import GradingRequest, GradingResponse

router = APIRouter()

@router.post("/grade", response_model=GradingResponse)
async def grade_speech(req: GradingRequest):
    base64_to_wav(req.recordingAudioBytes, "app/resources/recording.wav")

    result = pronunciation_assessment(req.refText, req.targetLanguage)
    return {
        "result": result
    }