def main():
    plate = input("Plate: ")
    if is_valid(list(plate)):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False 
    first = True
    for i in range(len(s)):
        if s[i].isdigit():
            #print(s[i])
            if first == True:
                first = False
                if s[i] == "0":
                    return False
        elif first == False and  not s[i].isdigit():
                return False
        elif s[i].isalpha() == False and not s[i].isdigit():
                return False
    return True

if __name__ == "__main__":
    main()