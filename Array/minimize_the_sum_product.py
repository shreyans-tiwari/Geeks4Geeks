"""
You are given two arrays, A and B, of equal size N. The task is to find the minimum value of
A[0] * B[0] + A[1] * B[1] + .... + A[N-1] * B[N-1], where shuffling of elements of arrays A and B is allowed.
"""

n = 5
a = [6, 1, 9, 5, 4]
b = [3, 4, 8, 2, 4]

a.sort()
b.sort(reverse=True)
min_sum = 0

for i in range(n):
    min_sum += a[i] * b[i]

print(min_sum)
