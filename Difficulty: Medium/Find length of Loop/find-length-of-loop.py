'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        #code here
        if not head :
            return 0
        s=f=head
        c = 0
        while f and f.next :
            s = s.next
            f = f.next.next
            if s==f:
                return self.lc(s)
        return 0
        
    def lc(self,mn):
        curr = mn
        c = 1
        
        while curr.next!=mn:
            
            curr=curr.next
            c+=1
        return c
            
        
            