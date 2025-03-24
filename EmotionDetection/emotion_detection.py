import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers = header)
    formatted = json.loads(response.text)
    emotions_score = {
        'anger': formatted['emotionPredictions'][0]['emotion']['anger'],
        'disgust': formatted['emotionPredictions'][0]['emotion']['disgust'],
        'fear': formatted['emotionPredictions'][0]['emotion']['fear'],
        'joy': formatted['emotionPredictions'][0]['emotion']['joy'],
        'sadness': formatted['emotionPredictions'][0]['emotion']['sadness'],        
        }
    dominant_emotion = {'dominant_emotion': "None"}
    high_score = 0
    for emotion in emotions_score:
        if emotions_score[emotion] > high_score:
            high_score = emotions_score[emotion]
            dominant_emotion['dominant_emotion'] = emotion
    emotions_score.update(dominant_emotion)
    return emotions_score