import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url = url, json = myobj, headers=headers)
    
    response_data = response.json()
    emotion_predictions = response_data.get("emotionPredictions", [])

    # Extract emotions
    emotions = emotion_predictions[0].get("emotion", {})
    anger_score = emotions.get("anger", 0)
    disgust_score = emotions.get("disgust", 0)
    fear_score = emotions.get("fear", 0)
    joy_score = emotions.get("joy", 0)
    sadness_score = emotions.get("sadness", 0)

# Construct the emotion scores dictionary
    emotion_scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score
    }

    # Find the highest emotion
    highest_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return the result
    return {
        "emotion_scores": emotion_scores,
        "highest_emotion": highest_emotion
    }