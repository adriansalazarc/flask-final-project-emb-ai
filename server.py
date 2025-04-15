import json
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def render_emotion_detection():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "<b>Invalid text! Please try again!</b>"

    new_response = response.copy()
    del new_response["dominant_emotion"]
    formatted_response = json.dumps(new_response).replace("{", "").replace("}", "").replace('"',"'")
    return ("For the given statement, the system response is " + 
    formatted_response + 
    ". The dominant emotion is " + 
    "<b>" + 
    response['dominant_emotion'] + "</b>" + ".")

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5400)