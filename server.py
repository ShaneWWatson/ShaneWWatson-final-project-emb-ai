from flask import Flask, request, jsonify, render_template
import json
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detection():
    if request.method == 'POST':
        # Parse the incoming data
        data = request.json
        input_text = data.get("text", "")

        if not input_text:
            return jsonify({"error": "No text provided."}), 400

    else:  # Handle GET request
        input_text = request.args.get("textToAnalyze", "")

        if not input_text:
            return jsonify({"error": "No text provided."}), 400

    # Real emotion analysis (Replace mock with actual logic)
    detected_emotions = emotion_detector(input_text)
    try:
        emotion_scores = detected_emotions.get("emotion_scores", {})
        dominant_emotion = detected_emotions.get("highest_emotion", "unknown")
        
        if not emotion_scores:
            raise ValueError("Invalid emotion scores")

   
        # Prepare the response in the required format
        system_response = (
            f"For the given statement, the system response is 'anger': {emotion_scores['anger']}, "
            f"'disgust': {emotion_scores['disgust']}, 'fear': {emotion_scores['fear']}, "
            f"'joy': {emotion_scores['joy']} and 'sadness': {emotion_scores['sadness']}. "
            f"The dominant emotion is {dominant_emotion}."
        )
        
        return system_response
    except (TypeError, ValueError, KeyError) as e:
        return f"Error processing emotion data: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
