import sys
import os

def read_lines():
    file_name = sys.argv[1]
    file_name = file_name.strip()
    
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if not file_name.endswith(".py"):
        sys.exit("Not a Python file")
        
    if not os.path.exists(file_name):
        sys.exit("File does not exist")

    with open(file_name, 'r') as f:
        lines = f.readlines()

    filtered = []
    for line in lines:
        stripped = line.strip()
        if stripped == "":
            continue
        if stripped.startswith("#"):
            continue
        filtered.append(line)

    return len(filtered)
    
def main():
    print(read_lines())

if __name__ == "__main__":
    main()