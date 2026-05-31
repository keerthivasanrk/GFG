'''
structure of a linked list node 
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def insertInMiddle(self, head, x):
        #code here
        if not head :
            return Node(x)
            
        f = s  = head
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
        
        nn = Node(x)
        
        nn.next = s.next
        s.next = nn
        
        return head
        
        