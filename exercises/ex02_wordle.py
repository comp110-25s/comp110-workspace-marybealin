"Let's play a fun little guessing game :)"

__author__: str = "730485762"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    while turns <= 6:
        print(f"===Turn {turns}/6===")
        your_guess: str = input_guess(length=len(secret))
        print(emojified(guess=your_guess, secret=secret))
        if your_guess == secret:
            return print(f"You won in {turns}/6 turns!")
        turns += 1
    return print("X/6 - Sorry, try again tomorrow!")


def contains_char(secret: str, char: str) -> bool:
    """sees if the letter is in the secret word"""
    assert len(char) == 1, f"len('{char}') is not 1"
    idx: int = 0
    while idx < len(secret):
        if char == secret[idx]:
            return True
        idx += 1

    return False


def emojified(guess: str, secret: str) -> str:
    """Assigns emojis based on character correctness"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret), "Guess must be same length as secret"

    idx: int = 0
    result: str = ""
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            result += GREEN_BOX
        elif contains_char(secret=secret, char=guess[idx]) is False:
            result += WHITE_BOX
        else:
            result += YELLOW_BOX
        idx += 1
    return result


def input_guess(length: int) -> str:
    """Let's player know if the number of characters in their guess is wrong"""
    guess = input(f"Enter a {length} character word")
    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again:")
    return guess


if __name__ == "__main__":
    main(secret="codes")
