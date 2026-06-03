'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
'''
    head1:  head of linkedList 1
    head2:  head of linkedList 2
    n1:  len of  linkedList 1
    n2:  len of linkedList 1
    x:   given sum
'''
class Solution:
    def countPairs(self, head1, head2, x):
        # code here
        hs = set()
        l1 = head1
        while l1:
            hs.add(l1.data)
            l1 = l1.next
        l2 = head2
        c = 0
        
        while l2:
            cs = x-l2.data 
            if cs in hs:
                c+=1
            l2=l2.next
        return c