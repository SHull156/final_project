from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # retrieve test to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # pass text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # extract the emotion and score, return formatted string
    if response:
        return (f"For the given statement, the system response is "
                f"'anger': {response['anger']}, "
                f"'disgust': {response['disgust']}, "
                f"'fear': {response['fear']}, "
                f"'joy': {response['joy']} and "
                f"'sadness': {response['sadness']}. "
                f"The dominant emotion is {response['dominant_emotion']}.")
    else:
        return "Invalid input or could not detect emotion."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
