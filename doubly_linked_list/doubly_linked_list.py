"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""

#Node construtor
    # properties:
        # value / prev / next
    # methods : 
        # insert_after
        # insert_before
        # delete

#LinkeListDouble
    # properties : head, tail, length
    # methods :
        # len - returns length of the LL
        # add_to_head - creates a node and adds the head of the queue / take care of old node placement
        # remove_from_head
        # add_to_tail
        # remove_from_tail
        # move_to_f
        # get_max - highest value of list

class Node:
    def __init__(self,val):
        self.value = val
        self.next = None
        self.prev = None  #the prev property for each nodes turns it into a doubly linked list


class LinkeListDouble:
    # The DoublyLinkedList class itself should have the methods: add_to_head, add_to_tail, remove_from_head, remove_from_tail, move_to_front, move_to_end, delete, and get_max
    def __init__(self):
        self.head = None
        self.tail = None
    
    def show(self):
        n = self.head
        if n == None:
            print('there are no nodes in this linked list')
        while n != None:
            print(n.value)
            n = n.next

    def add_to_head(self,val):
        self.head = Node(val)
        print(f'set {self.head.value} as the head of the linkedlist')
    
    def add_to_tail(self,val):
        n = self.head
        self.tail = Node(val)
        while n.next != None:
            n = n.next
        n.next = self.tail
        print('tail of linked list: ', self.tail.value)


ll = LinkeListDouble()
ll.add_to_head(6)
ll.add_to_tail(7)
ll.add_to_tail(20)
ll.show()






    

















# class ListNode:
#     def __init__(self, value, prev=None, next=None):
#         self.value = value
#         self.prev = prev
#         self.next = next

#     """Wrap the given value in a ListNode and insert it
#     after this node. Note that this node could already
#     have a next node it is point to."""
#     def insert_after(self, value):
#         current_next = self.next
#         self.next = ListNode(value, self, current_next)
#         if current_next:
#             current_next.prev = self.next

#     """Wrap the given value in a ListNode and insert it
#     before this node. Note that this node could already
#     have a previous node it is point to."""
#     def insert_before(self, value):
#         current_prev = self.prev
#         self.prev = ListNode(value, current_prev, self)
#         if current_prev:
#             current_prev.next = self.prev

#     """Rearranges this ListNode's previous and next pointers
#     accordingly, effectively deleting this ListNode."""
#     def delete(self):
#         if self.prev:
#             self.prev.next = self.next
#         if self.next:
#             self.next.prev = self.prev


# """Our doubly-linked list class. It holds references to
# the list's head and tail nodes."""


# class DoublyLinkedList:
#     def __init__(self, node=None):
#         self.head = node
#         self.tail = node
#         self.length = 1 if node is not None else 0

#     def __len__(self):
#         return self.length

#     """Wraps the given value in a ListNode and inserts it 
#     as the new head of the list. Don't forget to handle 
#     the old head node's previous pointer accordingly."""
#     def add_to_head(self, value):
#         pass

#     """Removes the List's current head node, making the
#     current head's next node the new head of the List.
#     Returns the value of the removed Node."""
#     def remove_from_head(self):
#         pass

#     """Wraps the given value in a ListNode and inserts it 
#     as the new tail of the list. Don't forget to handle 
#     the old tail node's next pointer accordingly."""
#     def add_to_tail(self, value):
#         pass

#     """Removes the List's current tail node, making the 
#     current tail's previous node the new tail of the List.
#     Returns the value of the removed Node."""
#     def remove_from_tail(self):
#         pass

#     """Removes the input node from its current spot in the 
#     List and inserts it as the new head node of the List."""
#     def move_to_front(self, node):
#         pass

#     """Removes the input node from its current spot in the 
#     List and inserts it as the new tail node of the List."""
#     def move_to_end(self, node):
#         pass

#     """Removes a node from the list and handles cases where
#     the node was the head or the tail"""
#     def delete(self, node):
#         pass
        
#     """Returns the highest value currently in the list"""
#     def get_max(self):
#         pass
