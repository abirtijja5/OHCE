import datetime

# Configuration des langues
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

def get_time_index():
    """Retourne l'index selon l'heure de la journée"""
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        return 0  # matin
    elif 12 <= hour < 18:
        return 1  # après-midi
    else:
        return 2  # soir/nuit

def is_palindrome(text):
    """Vérifie si un texte est un palindrome (ignore la casse, espaces et ponctuation)"""
    # Garder seulement les lettres et chiffres, en minuscules
    import re
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return cleaned == cleaned[::-1] and len(cleaned) > 0

def reverse_text(text):
    """Renvoie le texte inversé (effet miroir)"""
    return text[::-1]

def main():
    """Fonction principale de l'application OHCE"""
    print("=== Application Console OHCE ===")
    
    # Sélection de la langue
    lang = input("Choisissez la langue (fr/en) : ").strip().lower()
    if lang not in LANGUAGES:
        print("Langue non supportée. Par défaut : français")
        lang = "fr"
    
    # Salutation de démarrage selon l'heure
    time_index = get_time_index()
    print(LANGUAGES[lang]["greetings"][time_index])
    print()
    
    # Boucle principale
    while True:
        try:
            user_input = input(LANGUAGES[lang]["prompt"]).strip()
            
            # Vérifier si l'utilisateur veut quitter
            if user_input.lower() in ["exit", "quit", "stop", "sortir"]:
                break
            
            # Si la saisie est vide, continuer
            if not user_input:
                continue
            
            # Effet miroir : renvoyer le texte inversé
            mirrored_text = reverse_text(user_input)
            print(mirrored_text)
            
            # Vérifier si c'est un palindrome
            if is_palindrome(user_input):
                print(LANGUAGES[lang]["palindrome"])
            
        except KeyboardInterrupt:
            print("\n")
            break
        except Exception as e:
            print(f"Erreur: {e}")
    
    # Salutation de fin selon l'heure
    time_index = get_time_index()
    print(LANGUAGES[lang]["farewells"][time_index])

if __name__ == "__main__":
    main()