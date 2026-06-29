import random
from ascii_art import STAGES


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"
         ]

def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)

def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    print("Welcome to Snowman Meltdown!")
    display_game_state(mistakes, secret_word, guessed_letters)



    while True:
        # For now, simply prompt the user once:
        guess = input("Guess a letter: ").lower()
        if len(guess) > 1:
            print('Sorry, too many characters.')
            continue
        if not isinstance(guess, str) or not guess.isalpha():
            print('Sorry not a valid input.')

        print("You guessed:", guess)
        if guess not in secret_word:
            mistakes += 1
        if mistakes == 4:
            print("ups, snowman kaputt.")
            break
        if guess in secret_word:
            guessed_letters.append(guess)
        display_game_state(mistakes, secret_word, guessed_letters)

        if len(set(guessed_letters)) == len(set(secret_word)):
            print('you saved the Snowman!')
            break
