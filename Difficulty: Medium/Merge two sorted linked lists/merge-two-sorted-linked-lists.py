'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self, head1, head2):
        # code here
        dum = Node(0)
        d = dum
        h1 = head1
        h2 = head2
        while h1 and h2:
            if h1.data<=h2.data:
                d.next = h1
                h1 = h1.next
                
            else:
                d.next = h2
                h2 = h2.next
                
            d = d.next
        if h1:
            d.next = h1
        if h2:
            d.next = h2
        
        return dum.next
                