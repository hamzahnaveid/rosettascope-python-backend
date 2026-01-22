from app.core.config import settings
import azure.cognitiveservices.speech as speechsdk
import base64

language_codes = {
    'en': 'en-US',
    'zh-cn': 'zh-CN-GUANGXI',
    'de': 'de-DE',
    'fr': 'fr-FR',
    'ko': 'ko-KR',
    'ja': 'ja-JP',
    'ru': 'ru-RU',
    'es': 'es-ES'
}

speech_config = speechsdk.SpeechConfig(
        subscription=settings.MICROSOFT_SPEECH_KEY,
        endpoint=settings.MICROSOFT_SPEECH_ENDPOINT
    )

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

def synthesize_speech(text: str, targetLanguage: str):
    speech_config.speech_synthesis_language = language_codes[targetLanguage]
    result = speech_synthesizer.speak_text_async(text).get()
    audio_data = result.audio_data
    return base64.b64encode(audio_data).decode("utf-8")