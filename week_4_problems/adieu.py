import sys
import inflect

p = inflect.engine()


def main():
    names = []

    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()  # Move to a new line after Ctrl+D
            break

    # p.join() joins names with commas and "and" automatically
    joined_names = p.join(names)
    print(f"Adieu, adieu, to {joined_names}")


if __name__ == "__main__":
    main()