'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self, head1, head2):
        # code here
        curr1 = head1
        curr2 = head2
        dummy = Node(0)
        gh = Node(0)
        gh.next = dummy
        while curr1 and curr2:
            if curr1.data>=curr2.data:
                
                dummy.next = curr2
                dummy = dummy.next
                curr2 = curr2.next
                
            else:
                dummy.next = curr1
                dummy = dummy.next
                curr1 = curr1.next
        while curr1 :
            dummy.next = curr1
            dummy = dummy.next
            curr1 = curr1.next
        while curr2:
            dummy.next = curr2
            dummy = dummy.next
            curr2 = curr2.next
            
        return gh.next.next