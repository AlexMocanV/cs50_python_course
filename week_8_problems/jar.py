import emoji

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = int(capacity)
        self._size = 0

    def __str__(self):
        s = ""
        for i in range(self._size):
            s += ":cookie:"
        return emoji.emojize(s)

    def deposit(self, n):
        if self._size + n <= self._capacity:
            self._size += n
        else :
            raise ValueError

    def withdraw(self, n):
        if self._size - n >= 0:
            self._size -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        return int(self._capacity)

    @property
    def size(self):
        return int(self._size)

def get_jar(capacity):
    return Jar(capacity)

def main():
    x = input()
    jarr = get_jar(x)
    jarr.deposit(3)
    print(jarr)

if __name__ == "__main__":
    main()