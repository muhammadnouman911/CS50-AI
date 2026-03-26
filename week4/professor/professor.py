import random


def main():
    level = get_level()

    score = 0

    for _ in range(0, 10):
        x = generate_integer(level)
        y = generate_integer(level)
        score += get_question_score(x, y)

    print(f"Score: {score}")


def get_question_score(x, y):
    correct_answer = x + y

    for _ in range(0, 3):
        try:
            answer = int(input(f"{x} + {y} = "))
        except ValueError:
            print("EEE")
            continue

        if answer == correct_answer:
            return 1

        print("EEE")

    print(f"{x} + {y} = {correct_answer}")
    return 0


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue

        if not (0 < level < 4):
            continue

        return level


def generate_integer(level):
    match level:
        case 1:
            a, b = 0, 9
        case 2:
            a, b = 10, 99
        case 3:
            a, b = 100, 999
        case _:
            raise ValueError()

    return random.randint(a, b)


if __name__ == "__main__":
    main()
