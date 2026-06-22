class Solution:
    def subLinkedList(self, head1, head2):  
        def remove_leading_zeros(head):
            while head and head.data == 0 and head.next:
                head = head.next
            return head
        
        def get_length(head):
            length = 0
            curr = head
            while curr:
                length += 1
                curr = curr.next
            return length
        
        l1 = remove_leading_zeros(head1)
        l2 = remove_leading_zeros(head2)
        
        # If both are entirely zeros, return a single node with value 0
        if not l1 or (l1.data == 0 and not l1.next):
            if not l2 or (l2.data == 0 and not l2.next):
                return Node(0)

        len1 = get_length(l1)
        len2 = get_length(l2)
        
        # Determine which linked list represents the larger numeric value
        if len1 > len2:
            larger, smaller = l1, l2
        elif len2 > len1:
            larger, smaller = l2, l1
        else:
            curr1, curr2 = l1, l2
            while curr1 and curr1.data == curr2.data:
                curr1 = curr1.next
                curr2 = curr2.next
            
            if not curr1:
                return Node(0)  # Both numbers are identical; difference is 0
            elif curr1.data > curr2.data:
                larger, smaller = l1, l2
            else:
                larger, smaller = l2, l1

        def rev(ll):
            curr = ll
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev  # Return moved outside the loop
        
        l1 = rev(larger)
        l2 = rev(smaller)
        
        dum = Node(0)
        curr = dum
        b = 0  # Borrow flag
        
        # Perform standard schoolbook subtraction from right to left
        while l1:
            val1 = l1.data
            val2 = l2.data if l2 else 0
            
            diff = val1 - val2 - b
            
            if diff < 0:
                diff += 10
                b = 1
            else:
                b = 0
                
            curr.next = Node(diff)  # Wrap data inside a Node object
            curr = curr.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return remove_leading_zeros(rev(dum.next))
