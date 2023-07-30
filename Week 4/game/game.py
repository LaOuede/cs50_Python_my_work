import random
import sys


def main():
    level = get_level()
    nb = random.randint(0, level)
    get_guess(nb)


def get_level():
    while True:
        try:
            lvl = int(input("Level: ").strip())
            if lvl <= 0:
                lvl = int(input("Level: ").strip())
            return lvl
        except ValueError:
            pass


def get_guess(nb):
    while True:
        try:
            guess = int(input("Guess: ").strip())
            if guess <= 0:
                guess = int(input("Guess: ").strip())
            if guess < nb:
                print("Too small!")
            elif guess > nb:
                print("Too large!")
            else:
                print("Just right!")
                sys.exit(0)
        except ValueError:
            pass


if __name__ == "__main__":
    main()
