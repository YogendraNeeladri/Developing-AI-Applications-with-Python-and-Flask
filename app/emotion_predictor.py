from .emotion_detector import detect_emotion

def emotion_predictor(text):
    result, status = detect_emotion(text)
    if status != 200:
        return result  # error dictionary
    
    # Format output
    formatted = {emotion: f"{round(score*100, 2)}%" for emotion, score in result.items()}
    return formatted

