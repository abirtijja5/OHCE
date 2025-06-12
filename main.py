from config import LANGUAGES
from ohce import OHCE


def main():
    lang = input("Choisissez la langue (fr/en) : ").strip().lower()
    if lang not in LANGUAGES:
        print("Langue non supportée. Par défaut : français")
        lang = "fr"
    
    app = OHCE(lang)
    app.run()


if __name__ == "__main__":
    main()