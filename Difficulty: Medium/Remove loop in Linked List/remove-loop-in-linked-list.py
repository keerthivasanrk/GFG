''' Structure of linked list Node
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''
class Solution:
    def removeLoop(self, head):
        if not head or not head.next:
            return
        
        s = f = head
        loop_exists = False
        
        # Step 1: Detect if a loop exists
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                loop_exists = True
                break
        
        # If no loop is found, do nothing
        if not loop_exists:
            return
        
        # Step 2: Find the last node and break the loop
        # Case A: The loop starts exactly at the head node
        if s == head:
            while f.next != head:
                f = f.next
            f.next = None
        
        # Case B: The loop starts somewhere in the middle
        else:
            s = head
            while s.next != f.next:
                s = s.next
                f = f.next
            f.next = None
