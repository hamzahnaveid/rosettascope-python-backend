from pydantic import BaseModel

class FeedbackRequest(BaseModel):
    json: str


class FeedbackResponse(BaseModel):
    feedback: str
