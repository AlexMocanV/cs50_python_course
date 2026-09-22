import random

def main():
    level = get_level()
    num = random.randint(1, level)

    guess = int(input("Guess: "))
    while guess != num: 
        if guess < num:
            print("Too small!")
        elif guess > num:
            print("Too large!")
        else:
            break
        guess = int(input("Guess: "))
    print("Just right!")

def get_level():
    while True:
        try:
            x = input("Level: ")
            if x.isdigit() and int(x) > 0:
                return int(x)
        except EOFError:
            break

if __name__ == "__main__": 
    main()