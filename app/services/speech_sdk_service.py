from app.core.config import settings
import azure.cognitiveservices.speech as speechsdk
import base64

# speech_config = speechsdk.SpeechConfig(
#         subscription=settings.MICROSOFT_SPEECH_KEY,
#         endpoint=settings.MICROSOFT_SPEECH_ENDPOINT
#     )

voice_names = {
    'de-DE': 'de-DE-KatjaNeural',
    'fr-FR': 'fr-FR-DeniseNeural',
    'es-ES': 'es-ES-ElviraNeural',
    'vi-VN': 'vi-VN-HoaiMyNeural',
    'zh-CN': 'zh-CN-XiaoxiaoNeural',
    'ar-SA': 'ar-SA-ZariyahNeural',
    'hi-IN': 'hi-IN-AnanyaNeural',
    'ko-KR': 'ko-KR-SunHiNeural',
    'ja-JP': 'ja-JP-NanamiNeural',
    'ru-RU': 'ru-RU-SvetlanaNeural',
    'sv-SE': 'sv-SE-SofieNeural',
    'fi-FI': 'fi-FI-SelmaNeural',
    'pl-PL': 'pl-PL-AgnieszkaNeural',
    'it-IT': 'it-IT-ElsaNeural',
    'nl-NL': 'nl-NL-FennaNeural'
}

# speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

def synthesize_speech(text: str, targetLanguage: str):
    speech_config = speechsdk.SpeechConfig(
        subscription=settings.MICROSOFT_SPEECH_KEY,
        endpoint=settings.MICROSOFT_SPEECH_ENDPOINT
    )

    speech_config.speech_synthesis_language = targetLanguage
    speech_config.speech_synthesis_voice_name = voice_names[targetLanguage]

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    result = speech_synthesizer.speak_text_async(text).get()
    audio_data = result.audio_data
    return base64.b64encode(audio_data).decode("utf-8")