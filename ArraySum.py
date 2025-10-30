def ArrSum(A,N):
    Sum = 0
    for i in range(N):
        Sum += A[i]
    return Sum
N = int(input())
A = list(map(int,input().split()))
print(ArrSum(A,N))

