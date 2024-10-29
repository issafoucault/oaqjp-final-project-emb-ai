"""
Emotion Detection Server

This module provides a Flask application for detecting emotions in text.
It exposes endpoints for analyzing text and rendering the main page.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    Analyze the emotion of input text.

    This endpoint takes a 'textToAnalyze' parameter from the query string,
    analyzes it using the emotion_detector function, and returns the results.

    :return: A formatted string with emotion scores and dominant emotion
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Error handling server
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    # Return a formatted string with the sentiment label and score
    return (
        f"For the given statement, the system response is 'anger':"
        f"{anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. " 
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Render the main index page.

    This endpoint serves the main HTML page of the application.

    :return: Rendered HTML template
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
