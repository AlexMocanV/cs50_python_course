def main():
    x = input("Greeting: ")
    x = x.split()
    print(value(x))
def value(greeting):
    if greeting[0].lower() == "hello":
        return 0
    elif greeting[0][0].lower() == "h":
        return 20
    else:
        return 100
if __name__ == "__main__":
    main()  

