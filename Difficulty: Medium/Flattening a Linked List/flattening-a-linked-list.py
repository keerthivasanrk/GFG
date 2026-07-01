'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
   
        # code here
         # 1. Helper function to merge two sorted bottom-linked lists
    def merge(self, a, b):
        if not a: return b
        if not b: return a
        
        # Compare data and link via the bottom pointer
        if a.data < b.data:
            result = a
            result.bottom = self.merge(a.bottom, b)
        else:
            result = b
            result.bottom = self.merge(a, b.bottom)
            
        # Ensure the next pointer is cleared as it's flattened
        result.next = None 
        return result
        
    # 2. Main function to flatten the list
    def flatten(self, root):
        # Base case: if list is empty or has only one node
        if not root or not root.next:
            return root
            
        # Recurse for the list on the right
        root.next = self.flatten(root.next)
        
        # Merge the current node's list with the flattened right list
        root = self.merge(root, root.next)
        
        return root