"""
class Node:
    def __init__(self, data):   
        self.data = data
        self.next = None
"""

class Solution:
    def cycleStart(self, head):
        #code here
        s=f=head
        
        while f and f.next:
            
            s=s.next
            f=f.next.next
            if s==f:
                s=head
                while s!=f:
                    s=s.next
                    f=f.next
                return s.data
                
        return -1