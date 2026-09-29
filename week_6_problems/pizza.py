import csv
import tabulate
import sys
import os

def write_menu(file_name):
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        print(tabulate.tabulate(reader, headers = "keys", tablefmt = "grid"))

def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    
    file_name = sys.argv[1]
    file_name = file_name.strip()
    
    if not file_name.endswith(".csv"):
        sys.exit("Not a CSV file")

    if not os.path.exists(file_name):
        sys.exit("File does not exist")

    write_menu(file_name)
    

if __name__ == "__main__":
    main()