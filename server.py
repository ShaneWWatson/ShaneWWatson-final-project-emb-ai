from flask import Flask, request, jsonify, render_template
import json
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detection():
    input_text = request.args.get("textToAnalyze", "")

    # if input_text == "":
    # return jsonify({"error": "No text provided."}), 400

    # Real emotion analysis (Replace mock with actual logic)
    detected_emotions = emotion_detector(input_text)
    try:
        emotion_scores = detected_emotions.get("emotion_scores", {})
        dominant_emotion = detected_emotions.get("highest_emotion", "unknown")
        print(f"TEST: {dominant_emotion}")
        
        if not emotion_scores:
            raise ValueError("Invalid emotion scores")

        if dominant_emotion == "None":
            raise ValueError("Invalid text! Please try again!")

   
        # Prepare the response in the required format
        system_response = (
            f"For the given statement, the system response is 'anger': {emotion_scores['anger']}, "
            f"'disgust': {emotion_scores['disgust']}, 'fear': {emotion_scores['fear']}, "
            f"'joy': {emotion_scores['joy']} and 'sadness': {emotion_scores['sadness']}. "
            f"The dominant emotion is {dominant_emotion}."
        )
        
        return system_response
    except (TypeError, ValueError, KeyError) as e:
        return f"Invalid text! Please try again!"

if __name__ == '__main__':
    app.run(debug=True)