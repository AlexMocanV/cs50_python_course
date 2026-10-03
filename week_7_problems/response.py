from validator_collection import checkers

def main():
    email_address = input("What's your email address?").strip()
    
    if checkers.is_email(email_address):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()