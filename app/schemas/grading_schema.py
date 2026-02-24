from pydantic import BaseModel

class GradingRequest(BaseModel):
    refText: str
    targetLanguage: str
    recordingAudioBytes: str
    confidenceMastered: float

class GradingResponse(BaseModel):
    result: str
    feedback: str
    new_confidence_mastered: float