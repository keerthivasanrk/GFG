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
        s=f=head
        if not head:
            return Node(x)
        
        while f.next and f.next.next:
            s=s.next
            f = f.next.next
        k = s.next    
        s.next = Node(x)
        s.next.next = k
        
        return head