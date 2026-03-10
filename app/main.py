from fastapi import FastAPI
from app.routers import translation_router
from app.routers import grading_router
from app.routers import feedback_router

app = FastAPI()

app.include_router(translation_router.router)
app.include_router(grading_router.router)
app.include_router(feedback_router.router)