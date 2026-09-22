def main():    
    x = input()
    print(shorten(x))

def shorten(x):
    result = ""
    for c in x:
        if c.lower() not in 'aeiou':
            result += c.lower()
    return result

if __name__ == "__main__":
    main()