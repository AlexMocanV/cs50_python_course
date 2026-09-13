def main():
    x = input()
    x = x.split()
    print(op(float(x[0]), x[1], float(x[2])))
def op(x, y, z):
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z
    else:
        return "Error"
main()