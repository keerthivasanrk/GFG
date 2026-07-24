'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    
    
    
    def m(self,l1,l2):
        if not l1: 
            return l2
        if not l2:
            return l1
            
            
        dum = Node(0)
        d = dum
        while l1 and l2:
            if l1.data<l2.data:
                d.bottom = l1
                l1=l1.bottom
                
            else:
                d.bottom = l2
                l2=l2.bottom
                
            d = d.bottom
            d.next = None
        if l1:
            d.bottom = l1
            
        if l2:
            d.bottom = l2
            
        return dum.bottom
            
        
    
    def flatten(self, root):
        if not root or not root.next:
            return root
            
        root.next = self.flatten(root.next)
        root =  self.m(root,root.next)
        
        return root
        
        
        
        
        
        
        
        
        
        