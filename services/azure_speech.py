import os
import azure.cognitiveservices.speech as speechsdk

from .utils import load_env


def recognize():
    load_env()
    SUBSCRIPTION_KEY = os.getenv('AZURE_SUBSCRIPTION_KEY')
    SERVICE_REGION = os.getenv('AZURE_SERVICE_REGION')
    speech_config = speechsdk.SpeechConfig(subscription=SUBSCRIPTION_KEY, region=SERVICE_REGION)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    print("Say something...")
    result = speech_recognizer.recognize_once()
    print(result)
