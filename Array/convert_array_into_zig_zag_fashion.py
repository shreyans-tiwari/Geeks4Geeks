"""
Given an array Arr (distinct elements) of size N. Rearrange the elements of array in zig-zag fashion.
The converted array should be in form a < b > c < d > e < f. The relative order of elements is same in the output
i.e you have to iterate on the original array only.
"""


def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


def zigZag(arr, n):
    for i in range(1, n, 2):
        if arr[i - 1] > arr[i]:
            swap(arr, i - 1, i)
        if i + 1 < n and arr[i + 1] > arr[i]:
            swap(arr, i + 1, i)


arr = [4, 3, 7, 8, 6, 2, 1]
zigZag(arr, len(arr))
print(arr)
