import math
def calc_sqrt(n):
    sqareRoot = math.sqrt(n)
    if sqareRoot >= 0:
        return sqareRoot
    else:
        return -1

n = int(input())
print(calc_sqrt(n))