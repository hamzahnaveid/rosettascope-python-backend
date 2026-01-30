import json
from app.core.config import settings
import azure.cognitiveservices.speech as speechsdk
import base64

speech_config = speechsdk.SpeechConfig(
        subscription=settings.MICROSOFT_SPEECH_KEY,
        region="westeurope"
    )

def pronunciation_assessment(refText: str, targetLanguage: str):
    speech_config.speech_recognition_language = targetLanguage

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

    audio_config = speechsdk.audio.AudioConfig(filename="app/resources/output.wav")
    
    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, 
        audio_config=audio_config, 
    )

    pronunciation_config.apply_to(speech_recognizer)

    result = speech_recognizer.recognize_once_async().get()
    if result.reason == speechsdk.ResultReason.Canceled:
        cancellation = speechsdk.CancellationDetails(result)
        print("Cancellation reason:", cancellation.reason)
        print("Error details:", cancellation.error_details)
        return None

    return result.properties.get(speechsdk.PropertyId.SpeechServiceResponse_JsonResult)
    