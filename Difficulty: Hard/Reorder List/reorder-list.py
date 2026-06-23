""" Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def reorderList(self, head):
        # code here
        f=s=head
        while f and f.next:
            s = s.next
            f=f.next.next
            
        prev = None
        curr = s.next
        s.next = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        f = head
        s = prev
        
        while s:
            t1 = f.next
            t2 = s.next
            f.next = s
            s.next = t1
            f = t1
            s = t2
            
        return head
        
            