"""
ou are required to complete two methods push() and pop(). The push() method takes one argument, an integer 'x' to be
pushed into the stack and pop() which returns an integer present at the top and popped out from the stack.
If the stack is empty then return -1 from the pop() method.
"""


class MyStack:
    class StackNode:

        # # Constructor to initialize a node
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None

    # Function to push an integer into the stack.
    def push(self, data):
        if self.top == None:
            self.top = self.StackNode(data)
        else:
            cur = self.StackNode(data)
            cur.next = self.top
            self.top = cur
        # Add code here

    # Function to remove an item from top of the stack.
    def pop(self):
        if self.top == None:
            return -1
        else:
            x = self.top.data
            self.top = self.top.next
            return x

        # Add code here


# {
#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = MyStack()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while (i < len(q1)):
            if (q1[i] == 1):
                s.push(q1[i + 1])
                i = i + 2
            elif (q1[i] == 2):
                print(s.pop(), end=" ")
                i = i + 1
            elif (s.isEmpty()):
                print(-1)
        print()

# } Driver Code Ends