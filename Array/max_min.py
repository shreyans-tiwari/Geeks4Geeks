"""Given an array A of size N of integers. Your task is to find the sum of minimum and maximum element in the array."""


def findSum(A, N):
    x = A[0]
    y = A[0]

    for i in range(N):
        if A[i] > x:
            x = A[i]
        if A[i] < y:
            y = A[i]

    return x + y


N = 5
A = [-2, 1, -4, 5, 3]
print(findSum(A, N))