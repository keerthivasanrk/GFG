'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def segregate(self, head):
        if not head or not head.next:
            return head
            
        # Create dummy nodes for three lists
        zero_dummy = Node(0)
        one_dummy = Node(0)
        two_dummy = Node(0)
        
        # Pointers to track the end of each list
        zero = zero_dummy
        one = one_dummy
        two = two_dummy
        
        # Traverse the original list
        curr = head
        while curr:
            if curr.data == 0:
                zero.next = curr
                zero = zero.next
            elif curr.data == 1:
                one.next = curr
                one = one.next
            else:
                two.next = curr
                two = two.next
            curr = curr.next
            
        # Combine the three lists
        # Link 0s list to 1s list if 1s exist, otherwise directly to 2s list
        zero.next = one_dummy.next if one_dummy.next else two_dummy.next
        # Link 1s list to 2s list
        one.next = two_dummy.next
        # Terminate the combined list
        two.next = None
        
        # The new head is the first node after the zero dummy node
        return zero_dummy.next
