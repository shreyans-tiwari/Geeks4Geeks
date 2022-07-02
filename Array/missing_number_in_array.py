"""
Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N.
Find the missing element.
"""
n = 10
array = [6, 1, 2, 8, 3, 4, 7, 10, 5]

res = n * (n + 1) // 2
for a in array:
    res -= a

print(res)
