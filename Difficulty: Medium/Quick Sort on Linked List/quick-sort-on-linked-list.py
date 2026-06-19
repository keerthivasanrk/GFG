''' Structure of linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
''' Structure of linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def quickSort(head):
    # Base case: if list is empty or has only one element
    if not head or not head.next:
        return head
        
    # Choose the first node as the pivot
    pivot = head
    curr = head.next
    
    # Dummy nodes to build smaller, equal, and greater partitions
    small_dummy = Node(0)
    equal_dummy = Node(0)
    greater_dummy = Node(0)
    
    small_tail = small_dummy
    equal_tail = equal_dummy
    greater_tail = greater_dummy
    
    # Place pivot into the equal partition
    equal_tail.next = pivot
    equal_tail = equal_tail.next
    
    # Partition the remaining nodes
    while curr:
        if curr.data < pivot.data:
            small_tail.next = curr
            small_tail = small_tail.next
        elif curr.data == pivot.data:
            equal_tail.next = curr
            equal_tail = equal_tail.next
        else:
            greater_tail.next = curr
            greater_tail = greater_tail.next
        curr = curr.next
        
    # Terminate lists to prevent cyclic pointers
    small_tail.next = None
    equal_tail.next = None
    greater_tail.next = None
    
    # Recursively sort the sublists
    sorted_small = quickSort(small_dummy.next)
    sorted_greater = quickSort(greater_dummy.next)
    
    # Concatenate: sorted_small -> equal partition -> sorted_greater
    if sorted_small:
        # Find the tail of the sorted smaller list
        temp = sorted_small
        while temp.next:
            temp = temp.next
        temp.next = equal_dummy.next
        new_head = sorted_small
    else:
        new_head = equal_dummy.next
        
    equal_tail.next = sorted_greater
    
    return new_head
