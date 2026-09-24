def get_int():
    while True:
        exp = input("Please enter an integer: ")
        try:
            exp = exp.split(sep = "/")
            if len(exp) != 2:
                raise ValueError
            x = int(exp[0])
            if x < 0:
                raise ValueError
            y = int(exp[1])
            if y < 0:
                raise ValueError
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise Exception
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        except Exception:
            pass 
        else: 
            break
    return (x, y)

def main():
    (x, y) = get_int()
    fraction = x * 100 / y
    if fraction <= 1:
        print("E")
    elif fraction >= 99:
        print("F")
    else:
        print(f"{fraction:.0f}%")

if __name__ == "__main__":
    main()