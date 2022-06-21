"""
Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not. Two arrays are said to
be equal if both of them contain same set of elements, arrangements (or permutation) of elements may be different
though.
Note : If there are repetitions, then counts of repeated elements must also be same for two array to be equal.
"""

N = 5
A = [1, 2, 5, 4, 0]
B = [2, 4, 5, 0, 1]
res = True
freq = {}
for i in range(N):
    if A[i] in freq:
        freq[A[i]] += 1
    else:
        freq[A[i]] = 1
    if B[i] in freq:
        freq[B[i]] -= 1
    else:
        freq[B[i]] = -1

for f in freq:
    if freq[f] != 0:
        res = False

print(res)