"""
You are given the head of a Linked List. You have to move the last element to the front of the
Linked List and return the list.
"""

"""
Definition
for singly Link List Node


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""


class Solution:

    def moveToFront(self, head):
        prev = head

        if prev.next == None:
            return prev

        cur = prev.next

        while cur.next != None:
            cur = cur.next
            prev = prev.next

        cur.next = head
        prev.next = None

        return cur
