import random
import sys


def get_level():
    while True:
        try:
            x = input("Level: ")
            if x.isdigit() and int(x) > 0:
                return int(x)
        except (EOFError, KeyboardInterrupt):
            sys.exit()
        except ValueError:
            pass


def get_guess():
    while True:
        try:
            x = input("Guess: ")
            if x.isdigit() and int(x) > 0:
                return int(x)
        except (EOFError, KeyboardInterrupt):
            sys.exit()
        except ValueError:
            pass


def main():
    level = get_level()
    num = random.randint(1, level)

    while True:
        guess = get_guess()

        if guess < num:
            print("Too small!")
        elif guess > num:
            print("Too large!")
        else:
            print("Just right!")
            break


if __name__ == "__main__":
    main()