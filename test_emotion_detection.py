import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        result1 = "joy"
        self.assertEqual(emotion_detector("I am glad this happened")['dominant_emotion'], result1)
        
        result2 = "anger"
        self.assertEqual(emotion_detector("I am really mad about this")['dominant_emotion'], result2)

        result3 = "disgust"
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")['dominant_emotion'], result3)

        result4 = "sadness"
        self.assertEqual(emotion_detector("I am so sad about this")['dominant_emotion'], result4)

        result5 = "fear"
        self.assertEqual(emotion_detector("I am really afraid that this will happen")['dominant_emotion'], result5)



unittest.main()
