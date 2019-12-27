# import sys
# sys.path.append('../doubly_linked_list')
# from doubly_linked_list import DoublyLinkedList

from dll import DLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DLinkedList()

    def push(self, value):
        self.storage.prepend(value)

    def pop(self):
        pass

    def len(self):
        pass
