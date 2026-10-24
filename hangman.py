"""
Hangman Game
CodeAlpha Python Programming Internship - Task 1

A simple text-based Hangman game. The computer picks a random word from a
small predefined list and the player guesses it one letter at a time.
The player loses after 6 incorrect guesses.
"""

import random

WORDS = ["python", "keyboard", "internet", "program", "developer"]
MAX_WRONG_GUESSES = 6

# ASCII drawings of the hangman, indexed by the number of wrong guesses (0-6)
HANGMAN_STAGES = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========""",
]


def display_status(secret_word, guessed_letters, wrong_guesses):
    """Print the hangman drawing, the word progress and the guesses so far."""
    print(HANGMAN_STAGES[len(wrong_guesses)])

    progress = ""
    for letter in secret_word:
        if letter in guessed_letters:
            progress += letter + " "
        else:
            progress += "_ "
    print("\nWord: " + progress.strip())

    if wrong_guesses:
        print("Wrong guesses: " + ", ".join(wrong_guesses))
    remaining = MAX_WRONG_GUESSES - len(wrong_guesses)
    print("Guesses left: " + str(remaining))


def get_guess(already_guessed):
    """Keep asking until the player enters a single new letter."""
    while True:
        guess = input("\nEnter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
        elif guess in already_guessed:
            print("You already guessed '" + guess + "'. Try a different letter.")
        else:
            return guess


def play_game():
    """Run one full round of Hangman."""
    secret_word = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses = []

    print("\n=== HANGMAN ===")
    print("Guess the word, one letter at a time. You can miss up to "
          + str(MAX_WRONG_GUESSES) + " times.")

    while len(wrong_guesses) < MAX_WRONG_GUESSES:
        display_status(secret_word, guessed_letters, wrong_guesses)

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess! '" + guess + "' is in the word.")
        else:
            wrong_guesses.append(guess)
            print("Sorry, '" + guess + "' is not in the word.")

        # Check for a win after every guess
        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations, you won! The word was '" + secret_word + "'.")
            return

    display_status(secret_word, guessed_letters, wrong_guesses)
    print("\nGame over! The word was '" + secret_word + "'.")


def main():
    """Play rounds until the player chooses to stop."""
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nGame closed. Goodbye!")
