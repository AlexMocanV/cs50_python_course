import sys

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}


def get_date():
    while True:
        try:
            x = input("Date: ").strip()
            # check if the input is empty
            # word month format

            if x and x[0].isalpha():
                # comma is mandatory 
                if "," not in x:
                    continue

                parts = x.split(" ")
                month_name = parts[0].capitalize()
                day_str = parts[1].replace(",", "")
                year_str = parts[2]

                if month_name not in months:
                    continue

                day = int(day_str)
                year = int(year_str)

                if day < 1 or day > 31:
                    continue

                return [year, months[month_name], day]

            elif "/" in x:
                parts = x.split("/")
                month = int(parts[0])
                day = int(parts[1])
                year = int(parts[2])

                if month < 1 or month > 12:
                    continue
                if day < 1 or day > 31:
                    continue

                return [year, month, day]

        except (EOFError, KeyboardInterrupt):
            sys.exit()
        except (ValueError, IndexError):
            pass
def main():
    t = get_date()
    print(f"{t[0]:04d}-{t[1]:02d}-{t[2]:02d}")


if __name__ == "__main__":
    main()