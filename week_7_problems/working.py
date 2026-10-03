import re
import sys


def main():
    print(convert(input("Hours: ")))

def check_time(hour1, minute1, hour2, minute2):
    if hour1 > 23 or hour2 > 23 or minute1 > 59 or minute2 > 59:
        raise ValueError
    
def convert(s):
    match = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s)
    if match:

        hour1 = int(match.group(1))
        if match.group(2):
            minute1 = int(match.group(2))
        else:
            minute1 = 0
        if match.group(3) == "PM" and hour1 != 12:
            hour1 += 12
        elif match.group(3) == "AM" and hour1 == 12:
            hour1 = 0

        hour2 = int(match.group(4))
        if match.group(5):
            minute2 = int(match.group(5))
        else:
            minute2 = 0
        if match.group(6) == "PM" and hour2 != 12:
            hour2 += 12
        elif match.group(6) == "AM" and hour2 == 12:
            hour2 = 0

        try:
            check_time(hour1, minute1, hour2, minute2)
        except ValueError:
            raise ValueError

        return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"
    raise ValueError


if __name__ == "__main__":
    main()