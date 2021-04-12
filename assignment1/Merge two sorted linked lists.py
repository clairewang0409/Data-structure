class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)



# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    dum = SinglyLinkedListNode(None)
    prev = dum

    while head1 and head2:
        if head1.data <= head2.data:
            prev.next = head1
            head1 = head1.next
        else:
            prev.next = head2
            head2 = head2.next

        prev = prev.next
        
    if head1 == None:
        prev.next = head2
    elif head2 == None:
        prev.next = head1
    
    return dum.next
 
