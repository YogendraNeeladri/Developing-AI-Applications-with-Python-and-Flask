from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Replace with your IBM Watson NLU API key & URL
API_KEY = 'YOUR_API_KEY'
URL = 'YOUR_URL'

authenticator = IAMAuthenticator(API_KEY)
nlp = NaturalLanguageUnderstandingV1(
    version='2023-08-01',
    authenticator=authenticator
)
nlp.set_service_url(URL)

def detect_emotion(text):
    if not text.strip():
        return {'error': 'Empty text provided'}, 400
    try:
        response = nlp.analyze(
            text=text,
            features=Features(emotion=EmotionOptions())
        ).get_result()
        return response['emotion']['document']['emotion'], 200
    except Exception as e:
        return {'error': str(e)}, 500

