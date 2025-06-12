import unittest
from unittest.mock import patch, MagicMock
from ohce import OHCE
from config import LANGUAGES
import utils

class TestOHCE(unittest.TestCase):
    
    def setUp(self):
        self.ohce_fr = OHCE("fr")
        self.ohce_en = OHCE("en")
    
    def test_initialization_french(self):
        self.assertEqual(self.ohce_fr.language, "fr")
        self.assertEqual(self.ohce_fr.lang_data, LANGUAGES["fr"])
    
    def test_initialization_english(self):
        self.assertEqual(self.ohce_en.language, "en")
        self.assertEqual(self.ohce_en.lang_data, LANGUAGES["en"])
    
    def test_initialization_invalid_language(self):
        ohce_invalid = OHCE("de")  
        self.assertEqual(ohce_invalid.language, "fr") 
    
    def test_reverse_text(self):
        self.assertEqual(self.ohce_fr.reverse_text("bonjour"), "ruojnob")
        self.assertEqual(self.ohce_fr.reverse_text("monde"), "ednom")
        self.assertEqual(self.ohce_fr.reverse_text("hello"), "olleh")
        self.assertEqual(self.ohce_fr.reverse_text(""), "")
    
    def test_palindrome_valid(self):
        self.assertTrue(self.ohce_fr.palindrome("kayak"))
        self.assertTrue(self.ohce_fr.palindrome("radar"))
        self.assertTrue(self.ohce_fr.palindrome("deed"))
        self.assertTrue(self.ohce_fr.palindrome("A man a plan a canal Panama"))
        self.assertTrue(self.ohce_fr.palindrome("Madam"))
    
    def test_palindrome_invalid(self):
        self.assertFalse(self.ohce_fr.palindrome("bonjour"))
        self.assertFalse(self.ohce_fr.palindrome("hello"))
        self.assertFalse(self.ohce_fr.palindrome("world"))
        self.assertFalse(self.ohce_fr.palindrome(""))
    
    @patch('utils.datetime')
    def test_get_time_index_morning(self, mock_datetime):
        mock_datetime.datetime.now.return_value.hour = 9
        self.assertEqual(self.ohce_fr.get_time_index(), 0)
    
    @patch('utils.datetime')
    def test_get_time_index_afternoon(self, mock_datetime):
        mock_datetime.datetime.now.return_value.hour = 15
        self.assertEqual(self.ohce_fr.get_time_index(), 1)
    
    @patch('utils.datetime')
    def test_get_time_index_evening(self, mock_datetime):
        mock_datetime.datetime.now.return_value.hour = 20
        self.assertEqual(self.ohce_fr.get_time_index(), 2)
    
    @patch('utils.datetime')
    def test_get_time_index_night(self, mock_datetime):
        mock_datetime.datetime.now.return_value.hour = 2
        self.assertEqual(self.ohce_fr.get_time_index(), 2)
    
    def test_should_quit_commands(self):
        quit_commands = ["exit", "quit", "stop", "sortir", "EXIT", "QUIT"]
        for cmd in quit_commands:
            self.assertTrue(self.ohce_fr.should_quit(cmd))
    
    def test_should_not_quit_commands(self):
        normal_commands = ["hello", "bonjour", "kayak", "test"]
        for cmd in normal_commands:
            self.assertFalse(self.ohce_fr.should_quit(cmd))
    
    @patch('builtins.print')
    def test_greet_french_morning(self, mock_print):
        with patch.object(self.ohce_fr, 'get_time_index', return_value=0):
            self.ohce_fr.greet()
            mock_print.assert_called_with("Bonjour")
    
    @patch('builtins.print')
    def test_greet_english_afternoon(self, mock_print):
        with patch.object(self.ohce_en, 'get_time_index', return_value=1):
            self.ohce_en.greet()
            mock_print.assert_called_with("Good afternoon")
    
    @patch('builtins.print')
    def test_farewell_french_evening(self, mock_print):
        with patch.object(self.ohce_fr, 'get_time_index', return_value=2):
            self.ohce_fr.farewell()
            mock_print.assert_called_with("Bonne nuit")
    
    @patch('builtins.print')
    def test_process_input_normal_text(self, mock_print):
        result = self.ohce_fr.process_input("hello")
        self.assertTrue(result)
        mock_print.assert_called_with("olleh")
    
    @patch('builtins.print')
    def test_process_input_palindrome(self, mock_print):
        result = self.ohce_fr.process_input("kayak")
        self.assertTrue(result)
        expected_calls = [unittest.mock.call("kayak"), unittest.mock.call("Bien dit !")]
        mock_print.assert_has_calls(expected_calls)
    
    @patch('builtins.print')
    def test_process_input_empty_string(self, mock_print):
        result = self.ohce_fr.process_input("")
        self.assertTrue(result)
        mock_print.assert_not_called()
    
    def test_languages_structure(self):
        for lang in ["fr", "en"]:
            self.assertIn("greetings", LANGUAGES[lang])
            self.assertIn("farewells", LANGUAGES[lang])
            self.assertIn("palindrome", LANGUAGES[lang])
            self.assertEqual(len(LANGUAGES[lang]["greetings"]), 3)
            self.assertEqual(len(LANGUAGES[lang]["farewells"]), 3)


class TestUtils(unittest.TestCase):
    
    @patch('utils.datetime')
    def test_utils_get_time_index_morning(self, mock_datetime):
        mock_datetime.datetime.now.return_value.hour = 9
        self.assertEqual(utils.get_time_index(), 0)
    
    @patch('utils.datetime')
    def test_utils_get_time_index_afternoon(self, mock_datetime):
        mock_datetime.datetime.now.return_value.hour = 15
        self.assertEqual(utils.get_time_index(), 1)
    
    @patch('utils.datetime')
    def test_utils_get_time_index_evening(self, mock_datetime):
        mock_datetime.datetime.now.return_value.hour = 20
        self.assertEqual(utils.get_time_index(), 2)
    
    def test_utils_is_palindrome_valid(self):
        self.assertTrue(utils.is_palindrome("kayak"))
        self.assertTrue(utils.is_palindrome("radar"))
        self.assertTrue(utils.is_palindrome("A man a plan a canal Panama"))
    
    def test_utils_is_palindrome_invalid(self):
        self.assertFalse(utils.is_palindrome("bonjour"))
        self.assertFalse(utils.is_palindrome("hello"))
        self.assertFalse(utils.is_palindrome(""))
    
    def test_utils_reverse_text(self):
        self.assertEqual(utils.reverse_text("hello"), "olleh")
        self.assertEqual(utils.reverse_text("world"), "dlrow")
        self.assertEqual(utils.reverse_text(""), "")
    
    def test_utils_should_quit(self):
        quit_commands = ["exit", "quit", "stop", "sortir"]
        for cmd in quit_commands:
            self.assertTrue(utils.should_quit(cmd))
        
        normal_commands = ["hello", "bonjour", "test"]
        for cmd in normal_commands:
            self.assertFalse(utils.should_quit(cmd))


if __name__ == '__main__':
    unittest.main()