import string
def main():
    x = input("Greeting: ")
    x = x.split()
    print(f"${check_greeting(x)}")

def check_greeting(greet):
    if greet[0].lower().rstrip(string.punctuation) == "hello":
        return 0
    elif greet[0][0].lower() == "h":
        return 20
    else:
        return 100
main()

