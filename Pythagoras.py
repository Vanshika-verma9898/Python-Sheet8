import math
def PythagorasTheorem(A,B):
    C = math.sqrt((A**2)+(B**2))
    return C
A = float(input())
B = float(input())
print(PythagorasTheorem(A,B))