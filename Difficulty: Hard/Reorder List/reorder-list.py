""" Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def rev(self, curr):
        prev  =None
        while curr:
            nn = curr.next
            curr.next = prev
            prev = curr
            curr = nn
            
        return prev
    
    
    def reorderList(self, head):
        # code here
        f = s= head
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
            
        h2  = s.next
        s.next = None
        revs = self.rev(h2)
        
        dum = Node(0)
        d = dum
        
        while head and revs:
            n1 = head.next
            n2  = revs.next
            d.next = head
            d = d.next
            d.next = revs
            d = d.next
            head = n1
            revs = n2
        
        if head:
            d.next = head
            
        return dum.next
            