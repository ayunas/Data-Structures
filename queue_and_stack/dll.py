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

    def __remove_node__(self,node):
        if node is self.head:
            # node.next = None
            self.head = self.head.next
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = None
        node.next = None
    
    def remove(self,val):
        found  = self.find(val)
        if found:
            self.__remove_node__(found)
        else:
            return
    
    def find(self,val):
        n = self.head
        while n and n.value != val:
            n = n.next
        return n

dll = DLinkedList()
dll.append(30)
dll.append(35)
dll.append(40)
dll.append(50)
dll.prepend(10)
dll.prepend(5)
print(dll)
dll.remove(30)
print(dll)






