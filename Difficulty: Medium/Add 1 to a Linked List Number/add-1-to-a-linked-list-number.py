''' structure of linked list Node
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def addOne(self, head):
        
        arr = []
        curr = head
        while curr:
            arr.append(curr.data)
            curr = curr.next
            
        
        arr = arr[::-1]
        na = []
        cr = 1
        for i in range(len(arr)):
            s = arr[i] + cr      
            cr = s // 10       
            s = s % 10         
            na.append(s)
            
        if cr > 0:
            na.append(cr)
            
        na = na[::-1]
        
        dummy = Node(0)
        dum = dummy
        for val in na:
            dum.next = Node(val)
            dum = dum.next
            
        return dummy.next 
