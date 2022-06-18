"""
Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.
"""
k = 3
arr = [1, 2, 3, 4, 5]
i = 0
while i < len(arr):
    m = i
    n = min(i+k-1, len(arr)-1)
    while m < n:
        arr[m], arr[n] = arr[n], arr[m]
        m += 1
        n -= 1
    i += k

print(arr)
