from game_logic import play_game, is_replay


def main():
    """Main flow of the program"""
    while True:
        play_game()
        if is_replay():
            break


if __name__ == "__main__":
    main()


