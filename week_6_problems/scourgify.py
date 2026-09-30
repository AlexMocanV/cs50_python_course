import csv
import sys
import os

def check_args():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    file_name = sys.argv[1]
     
    if not os.path.exists(file_name):
        sys.exit(f"Could not read {file_name}")
       
def main():
    check_args()

    with open(sys.argv[1], 'r', newline='') as input_file:
        reader = csv.DictReader(input_file)

        with open(sys.argv[2], 'w', newline='') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=['first','last','house'])
            writer.writeheader()

            for row in reader:
                name = row['name']
                name = name.split(' ')
                first = name[1].strip(', ""')
                last = name[0].strip(', ""')
                house = row['house']
                writer.writerows([{'first': first, 'last': last, 'house': house}])

if __name__ == "__main__":
    main()