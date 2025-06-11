import unittest
from unittest.mock import patch, MagicMock
from ohce import OHCE, LANGUAGES

class TestOHCE(unittest.TestCase):
    
    def setUp(self):
        """Prépare les tests avec une instance OHCE"""
        self.ohce_fr = OHCE("fr")
        self.ohce_en = OHCE("en")
    
    def test_initialization_french(self):
        """Test l'initialisation en français"""
        self.assertEqual(self.ohce_fr.language, "fr")
        self.assertEqual(self.ohce_fr.lang_data, LANGUAGES["fr"])
    
    def test_initialization_english(self):
        """Test l'initialisation en anglais"""
        self.assertEqual(self.ohce_en.language, "en")
        self.assertEqual(self.ohce_en.lang_data, LANGUAGES["en"])
    
    def test_initialization_invalid_language(self):
        """Test l'initialisation avec une langue invalide"""
        ohce_invalid = OHCE("de")  
        self.assertEqual(ohce_invalid.language, "fr") 
    
    def test_reverse_text(self):
        """Test la fonction d'inversion de texte"""
        self.assertEqual(self.ohce_fr.reverse_text("bonjour"), "ruojnob")
        self.assertEqual(self.ohce_fr.reverse_text("monde"), "ednom")
        self.assertEqual(self.ohce_fr.reverse_text("hello"), "olleh")
        self.assertEqual(self.ohce_fr.reverse_text(""), "")
    
    def test_palindrome_valid(self):
        """Test la détection de palindromes valides"""
        self.assertTrue(self.ohce_fr.palindrome("kayak"))
        self.assertTrue(self.ohce_fr.palindrome("radar"))
        self.assertTrue(self.ohce_fr.palindrome("deed"))
        self.assertTrue(self.ohce_fr.palindrome("A man a plan a canal Panama"))
        self.assertTrue(self.ohce_fr.palindrome("Madam"))
    
    def test_palindrome_invalid(self):
        """Test la détection de non-palindromes"""
        self.assertFalse(self.ohce_fr.palindrome("bonjour"))
        self.assertFalse(self.ohce_fr.palindrome("hello"))
        self.assertFalse(self.ohce_fr.palindrome("world"))
        self.assertFalse(self.ohce_fr.palindrome(""))
    
    def test_get_time_index_morning(self):
        """Test l'index du temps pour le matin"""
        with patch('datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value.hour = 9
            self.assertEqual(self.ohce_fr.get_time_index(), 0)
    
    def test_get_time_index_afternoon(self):
        """Test l'index du temps pour l'après-midi"""
        with patch('datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value.hour = 15
            self.assertEqual(self.ohce_fr.get_time_index(), 1)
    
    def test_get_time_index_evening(self):
        """Test l'index du temps pour le soir"""
        with patch('datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value.hour = 20
            self.assertEqual(self.ohce_fr.get_time_index(), 2)
    
    def test_get_time_index_night(self):
        """Test l'index du temps pour la nuit"""
        with patch('datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value.hour = 2
            self.assertEqual(self.ohce_fr.get_time_index(), 2)
    
    def test_should_quit_commands(self):
        """Test la détection des commandes de sortie"""
        quit_commands = ["exit", "quit", "stop", "sortir", "EXIT", "QUIT"]
        for cmd in quit_commands:
            self.assertTrue(self.ohce_fr.should_quit(cmd))
    
    def test_should_not_quit_commands(self):
        """Test que les commandes normales ne quittent pas"""
        normal_commands = ["hello", "bonjour", "kayak", "test"]
        for cmd in normal_commands:
            self.assertFalse(self.ohce_fr.should_quit(cmd))
    
    @patch('builtins.print')
    def test_greet_french_morning(self, mock_print):
        """Test la salutation française du matin"""
        with patch.object(self.ohce_fr, 'get_time_index', return_value=0):
            self.ohce_fr.greet()
            mock_print.assert_called_with("Bonjour")
    
    @patch('builtins.print')
    def test_greet_english_afternoon(self, mock_print):
        """Test la salutation anglaise de l'après-midi"""
        with patch.object(self.ohce_en, 'get_time_index', return_value=1):
            self.ohce_en.greet()
            mock_print.assert_called_with("Good afternoon")
    
    @patch('builtins.print')
    def test_farewell_french_evening(self, mock_print):
        """Test l'au revoir français du soir"""
        with patch.object(self.ohce_fr, 'get_time_index', return_value=2):
            self.ohce_fr.farewell()
            mock_print.assert_called_with("Bonne nuit")
    
    @patch('builtins.print')
    def test_process_input_normal_text(self, mock_print):
        """Test le traitement d'un texte normal"""
        result = self.ohce_fr.process_input("hello")
        self.assertTrue(result)
        mock_print.assert_called_with("olleh")
    
    @patch('builtins.print')
    def test_process_input_palindrome(self, mock_print):
        """Test le traitement d'un palindrome"""
        result = self.ohce_fr.process_input("kayak")
        self.assertTrue(result)
        expected_calls = [unittest.mock.call("kayak"), unittest.mock.call("Bien dit !")]
        mock_print.assert_has_calls(expected_calls)
    
    @patch('builtins.print')
    def test_process_input_empty_string(self, mock_print):
        """Test le traitement d'une chaîne vide"""
        result = self.ohce_fr.process_input("")
        self.assertTrue(result)
        mock_print.assert_not_called()
    
    def test_languages_structure(self):
        """Test la structure des données de langue"""
        for lang in ["fr", "en"]:
            self.assertIn("greetings", LANGUAGES[lang])
            self.assertIn("farewells", LANGUAGES[lang])
            self.assertIn("palindrome", LANGUAGES[lang])
            self.assertEqual(len(LANGUAGES[lang]["greetings"]), 3)
            self.assertEqual(len(LANGUAGES[lang]["farewells"]), 3)

if __name__ == '__main__':
    unittest.main()