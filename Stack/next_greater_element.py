"""
Given an array arr[ ] of size n having distinct elements,
the task is to find the next greater element for each element of the array
in order of their appearance in the array.
Next greater element of an element in the array is
the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element,
then next greater element for current element is -1.
For example, next greater of the last element is always -1.
"""

n = 5
arr = [6, 8, 0, 1, 3]

res = [-1 for i in range(n)]
stk = []
        
for i in range(n):
    if not stk or arr[i] <= arr[stk[-1]]:
        stk.append(i)
    else:
        while stk and arr[i] > arr[stk[-1]]:
            res[stk.pop()] = arr[i]
        stk.append(i)
                
print(res)
