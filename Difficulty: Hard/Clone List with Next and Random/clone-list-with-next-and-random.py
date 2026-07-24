'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.random = None
'''        

class Solution:
    def cloneLinkedList(self, head):
        # code here
        if not head :
            return head
            
        curr = head
        
        while curr:
            cl = Node(curr.data)
            cl.next = curr.next
            curr.next = cl
            curr = cl.next
            
        curr = head
        
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        curr = head
        clh = curr.next
        
        
        while curr:
            cln = curr.next
            curr.next = cln.next
            if cln.next :
                cln.next = cln.next.next
            curr = curr.next
        return clh
        