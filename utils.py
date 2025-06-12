import datetime
import re


def get_time_index():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        return 0  # matin
    elif 12 <= hour < 18:
        return 1  # après-midi
    else:
        return 2  # soir/nuit


def is_palindrome(input_string):
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', input_string).lower()
    return cleaned == cleaned[::-1] and len(cleaned) > 0


def reverse_text(text):
    return text[::-1]


def should_quit(user_input):
    quit_commands = ["exit", "quit", "stop", "sortir"]
    return user_input.lower().strip() in quit_commands