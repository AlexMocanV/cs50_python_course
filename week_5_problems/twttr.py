def main():    
    x = input("Input:")
    print(shorten(x))

def shorten(x):
    result = ""
    for c in x:
        if c.lower() not in 'aeiou':
            result += c
    return result

if __name__ == "__main__":
    main()