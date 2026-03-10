from pydantic import BaseModel

class FeedbackRequest(BaseModel):
    feedbackJsonArray: str


class FeedbackResponse(BaseModel):
    feedback: str
