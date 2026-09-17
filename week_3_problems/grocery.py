grocery_list = {}
def get_items():
    while True:
        try:
            x = input().upper()
            if x == "":
                break
            if x in grocery_list:
                grocery_list[x] += 1
            else:
                grocery_list[x] = 1
        except EOFError:
            break
def list_items():
    for item, count in grocery_list.items():
        print(f"{count} {item}")

def main():
    get_items()
    list_items()
main()