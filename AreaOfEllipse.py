import math
def calc_AreaOfEllipse(A,B):
    EllipseArea = math.pi * (A/2) * (B/2)  # Divide by 2 since A and B are full axes
    return EllipseArea
A = float(input())
B = float(input())
print(calc_AreaOfEllipse(A,B))

