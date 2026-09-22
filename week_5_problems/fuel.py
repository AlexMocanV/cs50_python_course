def main():
    while True:
        fraction = input("Please enter an integer: ")
        try:
            rezult = convert(fraction)
            print(gauge(rezult[0] * 100 / rezult[1]))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    fraction = fraction.split(sep = "/")
    if len(fraction) != 2:
        raise ValueError
    x = int(fraction[0]) 
    y = int(fraction[1])
    if y == 0:
        raise ZeroDivisionError
    if y < 0 or x < 0 or x > y:
        raise ValueError
    return (x, y)

def gauge(percentage = int):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage:.0f}%"

if __name__ == "__main__":
    main()