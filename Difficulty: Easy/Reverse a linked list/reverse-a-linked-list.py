"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        # Code here
        curr = head
        prev = None
        while curr:
            nn = curr.next
            curr.next = prev
            prev = curr
            curr = nn
            
            
        return prev