"""
Given a array of N numbers, we need to maximize the sum of selected numbers. At each step, you need to select a number
Ai, delete one occurrence of Ai-1 (if exists), and Ai each from the array.
Repeat these steps until the array gets empty.
The problem is to maximize the sum of the selected numbers.
Note: Numbers need to be selected from maximum to minimum.
"""

n = 20
arr = [9, 15, 9, 3, 8, 4, 6, 17, 7, 11, 17, 7, 3, 18, 13, 9, 7, 12, 2, 8]

arr.sort(reverse=True)

freq_map = {}
i = 0
while i < n:
    freq_map[arr[i]] = 1
    while i + 1 < n and arr[i + 1] == arr[i]:
        freq_map[arr[i]] += 1
        i += 1
    i += 1

i = 0
s = 0
while i < n:
    if freq_map[arr[i]] > 0:
        s += arr[i]
        freq_map[arr[i]] -= 1
        if arr[i] - 1 in freq_map and freq_map[arr[i] - 1] > 0:
            freq_map[arr[i] - 1] -= 1

    i += 1
print(s)
