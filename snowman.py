from ascii_art import STAGES
from game_logic import get_random_word, display_game_state, play_game


def main():
    """Main flow of the program"""
    while True:
        play_game()
        if is_replay():
            break


if __name__ == "__main__":
    main()


