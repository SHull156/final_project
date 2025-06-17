from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=['GET'])
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze', '')
    result = emotion_detector(text_to_analyze)

    if result is None:
        return "An error occurred while processing the request.", 500

    # If all values are None, treat as bad input (blank or 400)
    if all(value is None for value in result.values()):
        return "Invalid or blank input provided.", 400

    return (f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}.")

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
