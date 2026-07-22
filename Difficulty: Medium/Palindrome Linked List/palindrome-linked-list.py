'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def isPalindrome(self, head):
        f = s = head
        if not head or not head.next:
            return True
        while f.next and f.next.next:
            s=s.next
            f = f.next.next
            
        prev = None
        while s:
            nn =s.next
            s.next = prev
            prev = s
            s = nn
        curr = head   
        while prev and curr:
            if prev.data != curr.data:
                return False
            prev = prev.next
            curr = curr.next 
                
        return True
            