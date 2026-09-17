months = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
}

def get_date():
    while True:
        try:
            x = input("Date: ")
            if x[0].isalpha():
                x = x.split(" ")
                x[1] = x[1].replace(",", "")
                if int(x[1]) > 31:
                    continue
                return ([int(x[2]), months[x[0]], int(x[1])])
            else: 
                x = x.split("/")
                if int(x[1]) > 31:
                    continue
                if int(x[0]) > 12:
                    continue
                return ([int(x[2]), int(x[0]), int(x[1])])
        except EOFError:
            pass
        except ValueError:
            pass
    return x    
def main():
    t = get_date()
    print(f"{t[0]:04}-{t[1]:02}-{t[2]:02}")
main()
