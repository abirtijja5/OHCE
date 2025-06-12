from config import LANGUAGES
from utils import get_time_index, is_palindrome, reverse_text, should_quit


class OHCE:
    def __init__(self, language="fr"):
        self.language = language if language in LANGUAGES else "fr"
        self.lang_data = LANGUAGES[self.language]
    
    def get_time_index(self):
        return get_time_index()
    
    def palindrome(self, input_string):
        return is_palindrome(input_string)
    
    def reverse_text(self, text):
        return reverse_text(text)
    
    def should_quit(self, user_input):
        return should_quit(user_input)
    
    def greet(self):
        time_index = self.get_time_index()
        print(self.lang_data["greetings"][time_index])
    
    def farewell(self):
        time_index = self.get_time_index()
        print(self.lang_data["farewells"][time_index])
    
    def process_input(self, user_input):
        if not user_input.strip():
            return True 
        
        # Effet miroir
        mirrored_text = self.reverse_text(user_input)
        print(mirrored_text)
        
        # Vérification palindrome et réponse
        if self.palindrome(user_input):
            print(self.lang_data["palindrome"])
        
        return True 
    
    def run(self):
        print("=== Application Console OHCE ===")
        
        self.greet()
        print()
        
        while True:
            try:
                user_input = input(self.lang_data["prompt"])
                
                if self.should_quit(user_input):
                    break
                
                self.process_input(user_input)
                
            except KeyboardInterrupt:
                print("\n")
                break
            except Exception as e:
                print(f"Erreur: {e}")
        
        self.farewell()