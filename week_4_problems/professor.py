import random

def main():
    level = get_level()
    _ = 0
    while _ < 10:
        repeat = 1
        x = generate_integer(level)
        y = generate_integer(level)
        ans = int(input(f"{x} + {y} = "))
        if ans != x + y:
            while ans != x + y and repeat < 3:
                print("EEE")
                ans = int(input(f"{x} + {y} = "))
                repeat += 1
            if repeat == 3:
                print("EEE")
                print(f"{x} + {y} = {x + y}")
        _ += 1
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                raise ValueError
            return level
        except ValueError:
            pass


def generate_integer(level):
    return random.randint(10 ** (level - 1), 10 ** level - 1)


if __name__ == "__main__":
    main()