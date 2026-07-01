'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    def merge(self,a,b):
        if not a: return b
        if not b: return a
        if a.data<b.data:
            res = a
            res.bottom = self.merge(a.bottom,b)
        else:
            res = b
            res.bottom =self.merge(a,b.bottom)
            
        res.next = None
        return res
        
    def flatten(self, root):
        # code here
        if not root or not root.next:
            return root
            
        root.next = self.flatten(root.next)
        
        root = self.merge(root,root.next)
        
        return root