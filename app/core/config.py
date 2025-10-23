from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MICROSOFT_SPEECH_KEY: str
    MICROSOFT_SPEECH_ENDPOINT: str

settings = Settings()
