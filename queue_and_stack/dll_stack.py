# import sys
# sys.path.append('../doubly_linked_list')
# from doubly_linked_list import DoublyLinkedList

from dll import DLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DLinkedList()

    def push(self, value):
        self.size = self.size + 1
        self.storage.prepend(value)
        # return self.storage.head.value

    def pop(self):
        if self.len() == 0:
            return None
        self.size = self.size - 1
        head_val = self.storage.head.value
        self.storage.remove(head_val)
        return head_val

    def len(self):
        return self.size
    
    def __repr__(self):
        return repr(self.storage)

s = Stack()
s.push(20)
s.push(30)
s.push(40)
s.pop()
print(s)
