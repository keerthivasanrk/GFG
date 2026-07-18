# Structure of a link list node
# class node:
#     def __init__(self):  
#         self.data = None
#         self.next = None

class Solution:
    def divide(self, head):
        # code here
        curr = head
        evenStart =evenEnd= oddStart = oddEnd = None
        
        while curr:
            if curr.data % 2 == 0:
                if evenStart is None:
                    evenStart = curr
                    evenEnd = evenStart
                else:
                    
                    evenEnd.next = curr
                    evenEnd = curr
            else:
                if oddStart is None:
                    oddStart = curr
                    oddEnd = oddStart
                else:
                    
                    oddEnd.next = curr
                    oddEnd = curr
                    
            curr = curr.next
            
        if evenStart is None or oddStart is None:
            return head
            
        evenEnd.next = oddStart
        oddEnd.next = None
            
        return evenStart