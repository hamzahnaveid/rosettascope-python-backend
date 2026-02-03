from pydantic import BaseModel

class GradingRequest(BaseModel):
    refText: str
    targetLanguage: str
    recordingAudioBytes: str

class GradingResponse(BaseModel):
    result: str
    feedback: str