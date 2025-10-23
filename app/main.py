from fastapi import FastAPI
from app.routers import translation_router

app = FastAPI()

app.include_router(translation_router.router)