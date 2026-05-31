'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def isPalindrome(self, head):
        # code here
        if not head or not head.next :
            return True
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow
        prev = None
        while curr:
            nn = curr.next
            curr.next = prev
            prev = curr
            curr = nn
        
        fv = head
        sv = prev
        
        while sv:
            if fv.data != sv.data:
                return False
            fv,sv = fv.next,sv.next
        return True
        