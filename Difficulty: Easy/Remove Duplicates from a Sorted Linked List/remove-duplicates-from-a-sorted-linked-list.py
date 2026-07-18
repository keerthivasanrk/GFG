''' Structure of linked list Node
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
def removeDuplicates(head):
    #code here
    curr = head
    while curr and curr.next:
        if curr.next.data == curr.data:
            curr.next = curr.next.next
            
        else:
            curr = curr.next
            
    return head