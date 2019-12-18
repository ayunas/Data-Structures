"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def display(self):
        n = self.head
        while n != None :
            print('\t')
            print(n.value)
            if n.prev:
                print('n.prev', n.prev.value)
            else:
                print('no prev value for', n.value)
            if n.next:
                print('n.next', n.next.value)
            else:
                print('no next value for ', n.value)
            
            n = n.next


    def add_to_head(self, value):
        old_head = self.head
        # old_next = self.head.next
        self.head = ListNode(value)
        self.head.next = old_head
        old_head.prev = self.head


    def remove_from_head(self):
        if self.head.next == None:
            self.head = None
        else:
            self.head = self.head.next

    def add_to_tail(self, value):
        n = self.head
        while n.next != None:
            prev = n
            n = n.next
            n.prev = prev

        n.next = ListNode(value)
        n.next.prev = n
        self.tail = n.next

    def remove_from_tail(self):
        pass

    def move_to_front(self, node):
        node.prev.next = node.next
        node.prev = None
        node.next = self.head
        self.head = node

        # print(node.prev.value)
        print(node.next.value)

        print('LRU node', node.value)
        # self.head = node
        print('new self.head', self.head.value, 'self.head.next', self.head.next.value)

    def move_to_end(self, node):
        pass

    def delete(self, node):
        pass

    def get_max(self):
        pass
