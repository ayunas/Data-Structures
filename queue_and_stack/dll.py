class Node:
    def __init__(self,val=None, prev=None, next=None):
        self.value = val
        self.next = next
        self.prev = prev
    
    def __repr__(self):
        return repr(self.value)


class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __repr__(self):
        nodes = []
        n = self.head
        while n:
            nodes.append(repr(n))
            n = n.next
        return '[' + ', '.join(nodes) + ']'

    def prepend(self, val):

        if self.head is None:
            self.head = Node(val)
        else:
            new_node = Node(val,None,self.head)
            self.head.prev = new_node
        self.head = new_node
    
    def append(self,val):
        if self.head is None:
            self.head = Node(val,None,None)
            self.tail = self.head
        else:
            self.tail.next = Node(val,self.tail,None)
            self.tail = self.tail.next
    
dll = DLinkedList()
dll.append(30)
dll.append(35)
dll.append(40)
dll.append(50)
dll.prepend(10)
dll.prepend(5)
# print(dll.head.next.next.prev)
print(dll)



