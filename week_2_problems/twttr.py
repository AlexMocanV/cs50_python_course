def main():    
    x = input()
    print(solve(x))
def solve(x):
    result = ""
    for c in x:
        if c.lower() not in 'aeiou':
            result += c
    return result
main()