from pydantic import BaseModel

class TrainingRequest(BaseModel):
    trainingWord: list[str]
    targetLanguage: str
    confidenceMastered: list[float]

class TrainingResponse(BaseModel):
    word: str
    translation: str
    speaking_text: str
    speaking_pronunciation_audio_base64: str
    listening_text: str
    listening_fluff_words: list[str]
    listening_pronunciation_audio_base64: str
    reading_text: str
    reading_answer: str

class TrainingBatchResponse(BaseModel):
    results: list[TrainingResponse]