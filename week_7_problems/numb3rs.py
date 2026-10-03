import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    
    if not match:
        return False
    
    for i in range(1, 5):
        # check for useless zeros at the beginning of the number
        if len(match.group(i)) > 1 and match.group(i).startswith('0'):
            return False
        
        if int(match.group(i)) > 255:
            return False
    
    return True

if __name__ == "__main__":
    main()