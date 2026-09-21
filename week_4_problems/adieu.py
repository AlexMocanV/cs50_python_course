def main():
    solve()
def solve():
    text = "Adieu, adieu, to "
    names = []
    while True:
        try:
            x = input("Name: ")
            names.append(x)
        except EOFError:
            break
    if len(names) == 1:
        print(f"{text}{names[0]}.")
    elif len(names) == 2:
        print(f"{text}{names[0]} and {names[1]}.")
    else:
        for name in names[:-1]:
            text += f"{name}, "
        text += f"and {names[-1]}."
        print(text)
main()