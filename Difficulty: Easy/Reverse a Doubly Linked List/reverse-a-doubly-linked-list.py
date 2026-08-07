""" Structure of Doubly Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        if not head or not head.next:
            return head
        curr = head
        prevn = None
        
        while curr:
            curr.prev,curr.next = curr.next, curr.prev
            prevn = curr
            curr = curr.prev
            
        return prevn
        
        