x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()
if x[0].isdigit():
    if int(x) == 42:
        print("Yes")
    else:
        print("No")
elif x.lower() == 'forty-two' or x.lower() == 'forty two':
    print("Yes")
else:
    print("No")