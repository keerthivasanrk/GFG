"""  list Node is as defined below:

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

"""

# complete this function
class Solution:
    def pairWiseSwap(self, head):
        if not head or not head.next:
            return head
        
        dum = Node(0)
        dum.next = head
        prev = dum
        
        while prev.next and prev.next.next:
            f = prev.next
            s = f.next
            
            f.next = s.next
            s.next = f
            prev.next = s
            prev = f
            
        return dum.next

            
        