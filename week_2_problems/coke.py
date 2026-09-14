due = 50
while(due > 0):
    print(f"Amount Due: {due}")
    x = input("Insert Coin: ")
    if x == "25":
        due -= 25
    elif x == "10":
        due -= 10
    elif x == "5":
        due -= 5

if(due < 0):
    print(f"Change Owed: {-due}")