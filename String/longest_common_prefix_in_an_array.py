"""
Given a array of N strings, find the longest common prefix among all strings present in the array.
"""
# arr = ['geeksforgeeks', 'geeks', 'geek', 'geezer']
arr = ['hello', 'world']

# My code
c = arr[0][0]
i = 0
flag = 0
res = ""

while i < len(arr[0]):
    c = arr[0][i]
    for word in arr:
        if i >= len(word) or c != word[i]:
            flag = 1
            break
    i += 1
    if flag:
        break
    else:
        res += c

if res == "":
    print("-1")
else:
    print(res)

"""
# Geeks for Geeks solution
# A Utility Function to find the common 
# prefix between strings- str1 and str2
def commonPrefixUtil(str1, str2):
    result = "";
    n1 = len(str1)
    n2 = len(str2)

    # Compare str1 and str2
    i = 0
    j = 0
    while i <= n1 - 1 and j <= n2 - 1:

        if (str1[i] != str2[j]):
            break

        result += str1[i]
        i += 1
        j += 1

    return (result)


# A Function that returns the longest 
# common prefix from the array of strings
def commonPrefix(arr, n):
    prefix = arr[0]

    for i in range(1, n):
        prefix = commonPrefixUtil(prefix, arr[i])

    return (prefix)
"""
