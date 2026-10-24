"""
Basic Rule-Based Chatbot
CodeAlpha Python Programming Internship - Task 4

A simple console chatbot. It reads what the user types, looks for known
words or phrases and replies with a predefined answer. The chat continues
until the user says goodbye.
"""

import string

BOT_NAME = "CodeBot"

GREETINGS = {"hello", "hi", "hey"}
GOODBYES = {"bye", "goodbye", "exit", "quit"}
THANKS = {"thanks", "thank", "thankyou"}


def clean_text(message):
    """Lowercase the message and remove punctuation so matching is easier."""
    message = message.lower().strip()
    return message.translate(str.maketrans("", "", string.punctuation))


def is_goodbye(message):
    """Return True if the user wants to end the chat."""
    words = clean_text(message).split()
    return any(word in GOODBYES for word in words)


def get_response(message):
    """Return the chatbot's reply for the given user message."""
    text = clean_text(message)
    words = text.split()

    if text == "":
        return "Please type something and I'll try to help."
    elif is_goodbye(message):
        return "Goodbye!"
    elif "how are you" in text:
        return "I'm fine, thanks!"
    elif any(word in GREETINGS for word in words):
        return "Hi!"
    elif "your name" in text or "who are you" in text:
        return "I'm " + BOT_NAME + ", a simple chatbot built with Python."
    elif "help" in words:
        return ("You can say: hello, how are you, what is your name, "
                "thanks, or bye.")
    elif any(word in THANKS for word in words):
        return "You're welcome!"
    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do."


def main():
    print("=== " + BOT_NAME.upper() + " ===")
    print("Hi, I'm " + BOT_NAME + ". Type 'help' for ideas or 'bye' to exit.\n")

    while True:
        user_message = input("You: ")
        print(BOT_NAME + ": " + get_response(user_message) + "\n")

        if is_goodbye(user_message):
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n" + BOT_NAME + ": Goodbye!")
