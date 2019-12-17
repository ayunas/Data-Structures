class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print("No nodes in the linked list")
            return
        else:
            n = self.head
            while n is not None:
                print(n.value)
                n = n.next
    
    def insert_at_start(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

ll = LinkedList()
ll.insert_at_start(15)
ll.insert_at_start(20)
ll.print_list()


