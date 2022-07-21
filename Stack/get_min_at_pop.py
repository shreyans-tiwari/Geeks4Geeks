"""
You are given an array A of size N.
You need to first push the elements of the array into a stack and then print minimum in the stack at each pop.
"""


# Function to push all the elements into the stack.
def _push(a, n):
    stk = []
    for i in a:
        stk.append(i)
    return stk


# Function to print minimum value in stack each time while popping.
def _getMinAtPop(stack):
    while stack:
        print(min(stack), end=" ")
        stack.pop()


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        stack =  _push(a,n) # our stack to be used
        _getMinAtPop(stack) # print elements of stack as required
        print()
