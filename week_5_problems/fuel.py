def main():
    while True:
        exp = input("Please enter an integer: ")
        try:
            fraction = convert(exp)
            percentage = gauge(fraction)
            break
        except (ValueError, ZeroDivisionError, Exception) as e:
            print(f"Error: {e}")
    print(percentage)

def convert(fraction):
    fraction = fraction.split(sep = "/")
    if len(fraction) != 2:
        raise ValueError
    x = int(fraction[0])
    if x < 0:
        raise ValueError
    y = int(fraction[1])
    if y < 0:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    
    return x / y * 100

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage:.0f}%"

if __name__ == "__main__":
    main()
