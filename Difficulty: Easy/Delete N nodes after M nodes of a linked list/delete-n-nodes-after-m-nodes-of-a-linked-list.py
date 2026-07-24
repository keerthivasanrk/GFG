# Structure of Linked List Node
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def linkdelete(self, head, n, m):
        # Code here
        if not head :
            return None
            
        curr = head
        
        for _ in range(m-1):
            if not curr:
                return head
            curr = curr.next
            
        if not curr :
            return head
            
        t = curr.next
        
        for  _ in range(n):
            if not t:
                break
            t = t.next
            
            
        curr.next = self.linkdelete(t,n,m)
        
        return head
                
        