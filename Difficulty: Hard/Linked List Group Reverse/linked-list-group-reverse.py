""" Structure of linked list Node
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""
class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        if not head:
            return None
            
        d = Node(0)
        d.next = head
        
        bg = d
        
        while True:
            if not bg.next:
                break
            
            prev = None
            curr = bg.next
            gh  = curr
            c =0 
            while curr and c<k:
                nn = curr.next
                curr.next = prev
                prev =curr
                curr = nn
                c+=1
                
            bg.next = prev
            gh.next = curr
            bg = gh
            
            
        return d.next
            
            