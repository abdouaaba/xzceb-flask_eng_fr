import unittest
from machinetranslation import translator

class TestTranslateEnToFr(unittest.TestCase):
    """
    Class to test the function english_to_french
    """
    def test1(self):
        """
        Function to test the function english_to_french
        """
        self.assertIsNone(translator.english_to_french(None))
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(translator.english_to_french("Bonjour"), "Hello")

class TestTranslateFrToEn(unittest.TestCase):
    """
    Class to test the function french_to_english
    """
    def test1(self):
        """
        Function to test the function french_to_english
        """
        self.assertIsNone(translator.french_to_english(None))
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(translator.french_to_english("Hello"), "Bonjour")

unittest.main()
