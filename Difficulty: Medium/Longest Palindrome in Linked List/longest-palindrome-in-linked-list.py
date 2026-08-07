"""Structure of a linked list node
class node:
    def __init__(self):
        self.data = None
        self.next = None
"""
class Solution:
    def countt(self, l,r):
        c = 0
        
        while l and r:
            if l.data == r.data:
                c+=1
                r = r.next
                l = l.next
                
            else:
                break
            
        return c

    def maxPalindrome(self,head):
        # Code here
        if not head:
            return 0
        if not head.next:
            return 1
            
        ml = 1
        prev = None
        curr = head
        
        while curr:
            
            nn = curr.next
            
            odd = self.countt(prev,curr.next)
            ml = max(ml,(odd*2)+1)
            
            even = self.countt(prev,curr)
            ml = max(ml,even*2)
            
            curr.next = prev
            prev = curr
            curr = nn
            
        self.rev(prev)
        return ml
        
    def rev(self, h1):
        c1 = h1
        p =None
        while c1:
            n1 = c1.next
            c1.next = p
            p = c1
            c1 = n1
            
        return p
        
        
        
        