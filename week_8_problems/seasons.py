from datetime import date
import re
import sys
import inflect

p = inflect.engine()
def validate_input(date_str):
    if re.search(r"^\d{4}-\d{2}-\d{2}$", date_str):
        try:
            date.fromisoformat(date_str)
            return True
        except ValueError:
            return False
    return False


def get_difference(date_str, today_date = None):
    past_date = date.fromisoformat(date_str)
    if today_date is None:
        today_date = date.today()
    days = (today_date - past_date).days
    return days * 24 * 60


def convert_to_words(minutes):
    words = p.number_to_words(minutes).replace(" and ", " ").capitalize()
    return f"{words} minutes"


def main():
    date_str = input("Date of Birth: ")
    if not validate_input(date_str):
        sys.exit(1)

    minutes = get_difference(date_str)
    print(convert_to_words(minutes))


if __name__ == "__main__":
    main()