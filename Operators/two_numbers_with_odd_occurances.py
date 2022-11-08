"""
Given an unsorted array, Arr[] of size N and that contains even number of occurrences for all numbers except two numbers.
Find the two numbers in decreasing order which has odd occurrences.
"""

def twoOddNum(Arr, N):
    freq = {}
    ans = []
        
    for a in Arr:
        if a in freq:
            freq[a] += 1
        else:
            freq[a] = 1
        
    for k in freq:
        if freq[k] % 2 != 0:
            ans.append(k)
        
    ans.sort(reverse=True)
    return ans


N = 8
Arr = [4, 2, 4, 5, 2, 3, 3, 1]

print(twoOddNum(Arr, N))
