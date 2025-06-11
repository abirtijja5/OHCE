import datetime
import re

LANGUAGES = {
    "fr": {
        "greetings": ["Bonjour", "Bon après-midi", "Bonsoir"],
        "farewells": ["Au revoir", "Bonne soirée", "Bonne nuit"],
        "palindrome": "Bien dit !",
        "choose_lang": "Choisissez la langue (fr/en) : ",
        "unsupported": "Langue non supportée. Par défaut : français",
        "prompt": ">>> "
    },
    "en": {
        "greetings": ["Good morning", "Good afternoon", "Good evening"],
        "farewells": ["Goodbye", "Have a nice evening", "Good night"],
        "palindrome": "Well said!",
        "choose_lang": "Choose language (fr/en) : ",
        "unsupported": "Unsupported language. Default: English",
        "prompt": ">>> "
    }
}

class OHCE:
    def __init__(self, language="fr"):
        """Initialise l'application OHCE avec la langue spécifiée"""
        self.language = language if language in LANGUAGES else "fr"
        self.lang_data = LANGUAGES[self.language]
    
    def get_time_index(self):
        """Retourne l'index selon l'heure de la journée"""
        hour = datetime.datetime.now().hour
        if 6 <= hour < 12:
            return 0  # matin
        elif 12 <= hour < 18:
            return 1  # après-midi
        else:
            return 2  # soir/nuit
    
    def palindrome(self, input_string):
        """Vérifie si un texte est un palindrome (ignore la casse, espaces et ponctuation)"""
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', input_string).lower()
        return cleaned == cleaned[::-1] and len(cleaned) > 0
    
    def reverse_text(self, text):
        """Renvoie le texte inversé (effet miroir)"""
        return text[::-1]
    
    def greet(self):
        """Affiche la salutation de début selon l'heure"""
        time_index = self.get_time_index()
        print(self.lang_data["greetings"][time_index])
    
    def farewell(self):
        """Affiche la salutation de fin selon l'heure"""
        time_index = self.get_time_index()
        print(self.lang_data["farewells"][time_index])
    
    def process_input(self, user_input):
        """Traite l'entrée utilisateur et affiche les réponses appropriées"""
        if not user_input.strip():
            return True 
        
        # Effet miroir
        mirrored_text = self.reverse_text(user_input)
        print(mirrored_text)
        
        # Vérification palindrome et réponse
        if self.palindrome(user_input):
            print(self.lang_data["palindrome"])
        
        return True 
    
    def should_quit(self, user_input):
        """Vérifie si l'utilisateur veut quitter"""
        quit_commands = ["exit", "quit", "stop", "sortir"]
        return user_input.lower().strip() in quit_commands
    
    def run(self):
        """Méthode principale qui lance l'application OHCE"""
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

def main():
    """Fonction principale pour lancer l'application"""
    lang = input("Choisissez la langue (fr/en) : ").strip().lower()
    if lang not in LANGUAGES:
        print("Langue non supportée. Par défaut : français")
        lang = "fr"
    
    app = OHCE(lang)
    app.run()

if __name__ == "__main__":
    main()