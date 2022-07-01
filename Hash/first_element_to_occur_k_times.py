"""
Given an array of N integers. Find the first element that occurs at least K number of times.
"""
n, k = 7, 2
a = [1, 7, 4, 3, 4, 8, 7]
freq = {}
res = -1
for i in a:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

    if freq[i] == k:
        res = i
        break

print(res)
