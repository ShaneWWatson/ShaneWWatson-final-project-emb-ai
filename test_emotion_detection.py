import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        text = "I am glad this happend."
        result = emotion_detector(text)
        self.assertIn('highest_emotion', result, 'joy')

    def test_anger(self):
        text = "I am realy mad about this."
        result = emotion_detector(text)
        self.assertIn('highest_emotion', result, 'anger')

    def test_disgust(self):
        text = "I feel disguested just hearing about this."
        result = emotion_detector(text)
        self.assertIn('highest_emotion', result, 'disgust')
        
    def test_sad(self):
        text = "I am so sad about this."
        result = emotion_detector(text)
        self.assertIn('highest_emotion', result, 'sadness')

    def test_sad(self):
        text = "I am really afraid that this will happen."
        result = emotion_detector(text)
        self.assertIn('highest_emotion', result, 'fear')

if __name__ == "__main__":
    unittest.main()