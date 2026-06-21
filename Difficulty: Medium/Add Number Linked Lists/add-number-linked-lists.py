'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def addTwoLists(self, head1, head2):
        
        def rev(ll):
            curr = ll
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
            
        l1 = rev(head1)
        l2 = rev(head2)
        
        dum = Node(0)
        cr = 0
        curr = dum
        
        while l1 or l2 or cr:
            v1  = l1.data if l1 else 0
            v2  = l2.data if l2 else 0
            t = v1+v2 + cr
            cr = t//10
            curr.next = Node(t%10)
            
            curr = curr.next
            if l1 : l1=l1.next
            if l2: l2 = l2.next
            
        res = rev(dum.next)
        while res and res.data == 0 and res.next:
            res = res.next
        return res