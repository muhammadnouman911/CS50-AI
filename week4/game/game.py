from random import randint
from sys import exit


def main():
    level = get_positive_int("Level: ")
    number = randint(1, level)

    while True:
        try:
            guess = get_positive_int("Guess: ")
        except ValueError:
            continue

        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            exit()


def get_positive_int(prompt):
    while True:
        try:
            n = int(input(prompt))
        except ValueError:
            continue

        if n > 0:
            return n


if __name__ == "__main__":
    main()
