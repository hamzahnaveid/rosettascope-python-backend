from app.core.config import settings
import azure.cognitiveservices.speech as speechsdk
import base64

speech_config = speechsdk.SpeechConfig(
        subscription=settings.MICROSOFT_SPEECH_KEY,
        endpoint=settings.MICROSOFT_SPEECH_ENDPOINT
    )

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

def synthesize_speech(text: str, targetLanguage: str):
    speech_config.speech_synthesis_language = targetLanguage
    result = speech_synthesizer.speak_text_async(text).get()
    audio_data = result.audio_data
    return base64.b64encode(audio_data).decode("utf-8")