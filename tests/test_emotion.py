import unittest
from app.emotion_predictor import emotion_predictor

class TestEmotionPredictor(unittest.TestCase):
    def test_valid_text(self):
        result = emotion_predictor("I am so happy today!")
        self.assertIn('joy', result)

    def test_empty_text(self):
        result = emotion_predictor("")
        self.assertEqual(result, {'error': 'Empty text provided'})

if __name__ == '__main__':
    unittest.main()

