from app.core.config import settings
import azure.cognitiveservices.speech as speechsdk
import base64

#language hard-coded to Spanish for test/demo purposes
def synthesize_speech(text: str, lang_code: str = "es-ES"):
    speech_config = speechsdk.SpeechConfig(
        subscription=settings.MICROSOFT_SPEECH_KEY,
        endpoint=settings.MICROSOFT_SPEECH_ENDPOINT
    )
    speech_config.speech_synthesis_language = lang_code
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    result = speech_synthesizer.speak_text_async(text).get()
    audio_data = result.audio_data
    return base64.b64encode(audio_data).decode("utf-8")