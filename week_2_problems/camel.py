def main():
    x = input("camelCase: ")
    # when i call list(x) it will convert the string into a list of characters
    print("snake_case: ", end="")
    print(snake(list(x)))

def snake(x):

    for i in range(len(x)):
        if x[i].isupper():
            x[i] =  "_" + x[i].lower() 
    #when i call "".join(x) it will convert the list of characters back into a string
    x = "".join(x)
    return x

main()

