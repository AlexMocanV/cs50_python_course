def main():
    x = input("What time is it? ")
    hour = convert(x)
    if hour >= 7 and hour <= 8.00:
        print("breakfast time")
    elif hour >= 12 and hour <= 13.00:
        print("lunch time")
    elif hour >= 18 and hour <= 19.00:
        print("dinner time")
    
def convert(x):
    y = x.split()
    time = y[0].split(sep = ":")
    hour = int(time[0]) + (int(time[1]) / 60)
    print(hour)
    if len(y) == 2:
        if y[1][0] == 'p' and int(time[0]) != 12:
            hour += 12
    return hour
if __name__ == "__main__":
    main()
