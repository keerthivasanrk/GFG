'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def intersectPoint(self, head1, head2):
        if not head1 or not head2:
            return None
            
        ptr1 = head1
        ptr2 = head2
       
        while ptr1 != ptr2:
            ptr1 = ptr1.next if ptr1 else head2
            ptr2 = ptr2.next if ptr2 else head1
            
        return ptr1