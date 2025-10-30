import math
def calc_VolumeOfSphere(A):
    if A <= 0:
        return "Radius must be a positive number."
    volume = (4/3) * math.pi * (A ** 3)
    return volume 
A = float(input())
print (calc_VolumeOfSphere(A))

