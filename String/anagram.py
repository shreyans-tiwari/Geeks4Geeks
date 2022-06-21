"""
Given two strings a and b consisting of lowercase characters. The task is to check whether two given strings are an
anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order
of characters can be different. For example, act and tac are an anagram of each other.
"""

# a = 'geeksforgeeks'
# b = 'forgeeksgeeks'
a = 'allergy'
b = 'allergic'

freq = {}
res = True

if len(a) != len(b):
    res = False

for i in range(len(a)):
    if a[i] in freq:
        freq[a[i]] += 1
    else:
        freq[a[i]] = 1

    if b[i] in freq:
        freq[b[i]] -= 1
    else:
        freq[b[i]] = -1

for key in freq:
    if freq[key] != 0:
        res = False

print(res)
