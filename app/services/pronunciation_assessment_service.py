import json
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
audio_config = speechsdk.audio.AudioConfig(filename="app/resources/recording.wav")

def pronunciation_assessment(refText: str, targetLanguage: str):
    enable_miscue, enable_prosody = True, False
    config_json = {
        "GradingSystem": "HundredMark",
        "Granularity": "Phoneme",
        "Dimension": "Comprehensive",
        "ScenarioId": "",
        "EnableMiscue": enable_miscue,
        "EnableProsodyAssessment": enable_prosody,
        "NBestPhonemeCount": 0,  # > 0 to enable "spoken phoneme" mode, 0 to disable
    }

    pronunciation_config = speechsdk.PronunciationAssessmentConfig(json_string=json.dumps(config_json))
    pronunciation_config.reference_text = refText

    language = language_codes[targetLanguage]
    
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, 
        audio_config=audio_config, 
        language=language
    )

    pronunciation_config.apply_to(speech_recognizer)

    result = speech_recognizer.recognize_once_async().get()
    return result.properties.get(speechsdk.PropertyId.SpeechServiceResponse_JsonResult)
    