
"""Flask web application for detecting emotions in user-provided text."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

APP = Flask(__name__)


@APP.route("/")
def index():
    """Render the application's home page."""
    return render_template("index.html")


@APP.route("/emotionDetector")
def detect_emotion():
    """Analyze user input and return the detected emotions."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    APP.run(host="localhost", port=5000, debug=True)
