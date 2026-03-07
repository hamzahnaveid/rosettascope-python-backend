from fastapi import APIRouter
from app.services.ollama_service import generate_feedback_aggregate
from app.schemas.feedback_schema import FeedbackRequest, FeedbackResponse

router = APIRouter()

router.post("/feedback", response_model=FeedbackResponse)
async def get_feedback(req: FeedbackRequest):
    feedback = generate_feedback_aggregate(req.json)
    return {
        "feedback": feedback
    }
