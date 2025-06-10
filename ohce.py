import datetime

# Détection de langue
LANGUAGES = {
    "fr": {
        "greetings": ["Bonjour", "Bonsoir", "Bonne nuit"],
        "farewells": ["Au revoir", "Bonne soirée", "Bonne nuit"],
        "palindrome": "Bien dit !"
    },
    "en": {
        "greetings": ["Good morning", "Good evening", "Good night"],
        "farewells": ["Goodbye", "Have a nice evening", "Good night"],
        "palindrome": "Well said!"
    }
}

def get_time_index():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return 0  # matin
    elif 12 <= hour < 18:
        return 1  # après-midi
    else:
        return 2  # soir/nuit

def is_palindrome(text):
    return text.lower() == text[::-1].lower()

def main():
    lang = input("Choisissez la langue (fr/en) : ").strip().lower()
    if lang not in LANGUAGES:
        print("Langue non supportée. Par défaut : français")
        lang = "fr"

    time_index = get_time_index()
    print(LANGUAGES[lang]["greetings"][time_index])

    while True:
        user_input = input(">>> ")
        if user_input.lower() in ["exit", "quit", "stop"]:
            break

        print(user_input[::-1])  # effet miroir

        if is_palindrome(user_input):
            print(LANGUAGES[lang]["palindrome"])

    print(LANGUAGES[lang]["farewells"][time_index])

if __name__ == "__main__":
    main()
