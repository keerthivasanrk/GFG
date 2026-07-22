''' structure of linked list Node
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def addOne(self,head):
        # code here
        h1 = self.rev(head)
        rh=h1
        carry = 1
        while h1:
            t = h1.data+carry
            carry = t // 10
            h1.data = t % 10
            if not h1.next and carry > 0:
                h1.next = Node(carry)
                carry = 0
                
            h1 = h1.next
            
        return self.rev(rh)
        
    def rev(self,l1):
        
        prev = None
        while l1:
            nn = l1.next
            l1.next = prev
            prev = l1
            l1 = nn
            
        return prev
        
        
        