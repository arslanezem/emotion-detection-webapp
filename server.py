'''
Emotion Detection Flask App

This Flask application provides an Emotion Detection service using the EmotionDetection module.
The app defines two routes:
- /emotionDetector: Accepts a text parameter (`textToAnalyze`) 
    and returns the emotion analysis result.
- /: Renders the index.html template.

Routes:
    - /emotionDetector:
        GET:
            Accepts a text parameter (`textToAnalyze`) through query parameters.
            Returns a formatted response containing emotion analysis results.
            If the dominant emotion is None, returns an error message.

    - /:
        GET:
            Renders the index.html template.

'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def emotion_dtr():
    '''
    Emotion Detector Route

    Accepts a text parameter (`textToAnalyze`) through query parameters.
    Returns a formatted response containing emotion analysis results.
    If the dominant emotion is None, returns an error message.

    Returns:
        str: Formatted response with emotion analysis results.
    '''
    emotion = request.args.get("textToAnalyze")
    response = emotion_detector(emotion)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )



@app.route("/")
def render_index_page():
    '''
    Index Page Route

    Renders the index.html template.

    Returns:
        Flask response: Rendered HTML template.
    '''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
