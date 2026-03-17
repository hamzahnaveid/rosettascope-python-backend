from typing import Annotated
from fastapi import APIRouter, Query
from app.services.ollama_service import generate_challenge_hints

router = APIRouter()

@router.get("/scavenger-hunt", response_model=str)
async def get_hints(words: Annotated[list[str] | None, Query()] = None):
    hints = generate_challenge_hints(words)
    return hints