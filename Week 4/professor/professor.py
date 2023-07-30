import random


def main():
    level = get_level()
    score = do_all(level)
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            lvl = int(input("Level: ").strip())
            if lvl in [1, 2, 3]:
                return lvl
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        min = 0
        max = 9
    elif level == 2:
        min = 10
        max = 99
    else:
        min = 100
        max = 999
    x = random.randint(min, max)
    y = random.randint(min, max)
    return x, y


def do_one(x, y, score):
    error = 0
    while error < 3:
        try:
            print(f"{x} + {y} = ", end="")
            res = int(input())
            if res == x + y:
                return score
            else:
                error += 1
                print("EEE")
        except:
            error += 1
            print("EEE")
    score -= 1
    print(f"{x} + {y} = {x + y}")
    return score


def do_all(level):
    exos = 0
    score = 10
    while exos < 10:
        x, y = generate_integer(level)
        score = do_one(x, y, score)
        exos += 1
    return score


if __name__ == "__main__":
    main()
