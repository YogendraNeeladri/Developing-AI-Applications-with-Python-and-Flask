from flask import Flask, request, jsonify
from app.emotion_predictor import emotion_predictor

app = Flask(__name__)

@app.route('/')
def index():
    return "Emotion Detection API is running!"

@app.route('/detect', methods=['POST'])
def detect():
    data = request.get_json()
    text = data.get('text', '')
    
    if not text.strip():
        return jsonify({'error': 'No text provided'}), 400
    
    result = emotion_predictor(text)
    
    if 'error' in result:
        return jsonify(result), 400
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

