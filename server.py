"""This is the main server for initializing flask and the server"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route('/')
def index():
    """Function to render the main page"""
    return render_template('index.html')

@app.route('/emotionDetector')
def detector():
    """Function to get the text from frontend, and return the response of the emotion detector"""
    text = request.args.get('textToAnalyze')
    response = emotion_detector(text)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger': {response['anger']},"
        f" 'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
