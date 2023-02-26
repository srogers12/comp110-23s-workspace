"""Exercise 3 Wordle."""

__author__ = "730466526"


def contains_char(secret: str, character: str) -> bool:
    """Finding the letter in the word."""
    assert len(character) == 1
    counter: int = 0
    while counter < len(secret):
        if secret[counter] == character:
            return True
        counter += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Inserts Emoji Colored Boxes."""
    assert len(guess) == len(secret)
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    emoji: str = ""
    idx: int = 0
    while idx < len(secret):
        if contains_char(secret, guess[idx]) is True:
            if guess[idx] == secret[idx]:
                emoji += green_box
            else:
                emoji += yellow_box
        else:
            emoji += white_box
        idx += 1
    return emoji


def input_guess(length: int) -> str:
    """Asks user for a correct in length guess."""
    guess: str = input(f"Enter a {length} character word: ")
    while len(guess) != length:
        guess_2: str = input(f"That wasn't {length} chars! Try again: ")
        guess = guess_2
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn: int = 1
    exit_loop: bool = False
    while turn <= 6 and exit_loop is False:
        print(f"=== Turn {turn}/6 ===")
        main_guess: str = input_guess(len(secret))
        print(emojified(main_guess, secret))
        if main_guess == secret:
            exit_loop = True
        else:
            turn += 1
    if main_guess == secret:
        print(f"You won in {turn}/6 turns!")
    if turn > len(secret):
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()