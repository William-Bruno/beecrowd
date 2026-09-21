n = int(input())

def is_even(a: int):
    if a % 2 == 0:
        return a+1
    else:
        return a+2

print(is_even(n))

