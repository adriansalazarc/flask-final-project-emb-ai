import requests, json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = myobj, headers=header)

    if(response.status_code == 400):
        return ({
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    })

    formatted_response = json.loads(response.text);
    
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    
    max_score = anger_score
    dominant_emotion = "anger"

    if(disgust_score > max_score):
        max_score = disgust_score
        dominant_emotion = "disgust"
    if(fear_score > max_score):
        max_score = fear_score
        dominant_emotion = "fear"
    if(joy_score > max_score):
        max_score = joy_score
        dominant_emotion = "joy"
    if(sadness_score > max_score):
        max_score = sadness_score
        dominant_emotion = "sadness"

    emotions_obj = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return emotions_obj