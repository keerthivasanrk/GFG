# Structure of Doubly Linked List Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def givenSumPairs(self, head, target):
        # code here
        ans = []
        if not head :
            return ans
        f= r = head
        while r.next:
            r = r.next
            
        while f!=r and r.next!=f:
            s = f.data+r.data
            if s==target:
                ans.append([f.data, r.data])
                f = f.next
                r = r.prev
            elif s>target:
                r = r.prev
            else:
                f = f.next
                
        return ans
        
        