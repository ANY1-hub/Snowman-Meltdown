import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"
         ]
# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
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
        print("You guessed:", guess)
        guessed_letters.append(guess)
        display_game_state(mistakes, secret_word, guessed_letters)

        if mistakes == 4:
            print("ups, snowman dead.")
            break
        if guess not in secret_word:
            mistakes += 1



if __name__ == "__main__":
    play_game()

