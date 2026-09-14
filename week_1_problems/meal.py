def main():
    x = input()
    meal(x)
def meal(x):
    y = x.split()
    time = y[0].split(sep = ":")
    if y[1][0] == 'a': 
        if int(time[0]) == 7 or (int(time[0]) == 8 and int(time[1]) == 0):
            print("breakfast time")
        elif int(time[0]) == 12: 
            print("lunch time")
    else :
        if (int(time[0]) == 1 and int(time[1]) == 0):
            print("lunch time")
        elif int(time[0]) == 6 or (int(time[0]) == 7 and int(time[1]) == 0):
            print("dinner time")
main()
