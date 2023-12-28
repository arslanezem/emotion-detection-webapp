import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = obj, headers=header)
    f_response = json.loads(response.text)

    if response.status_code == 400:
        output = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
            }
    else:
        emotion_dict = f_response['emotionPredictions'][0]['emotion']

        anger = emotion_dict['anger']
        disgust = emotion_dict['disgust']
        fear = emotion_dict['fear']
        joy = emotion_dict['joy']
        sadness = emotion_dict['sadness']
        dominant_emotion = max(emotion_dict, key=emotion_dict.get)

        output = {
                'anger': anger,
                'disgust': disgust,
                'fear': fear,
                'joy': joy,
                'sadness': sadness,
                'dominant_emotion': dominant_emotion
                }

    return output

