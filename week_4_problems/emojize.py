import emoji

def main():
    text = input("Input: ")
    print_emoji(text)
def print_emoji(text):
    print(f"Output: {emoji.emojize(text)}")

if __name__ == "__main__":
    main()