class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    def print_list(self):
        if self.start is None:
            print("No nodes in the linked list")
            return
        else:
            n = self.start
            while n is not None:
                print(n.value)
                n = n.next
    
    def insert_at_start(self,value):
        new_node = Node(value)
        new_node.next = self.start
        self.start = new_node
    
    def insert_after(self,node_value,value):
        if self.start == None:
            self.start = Node(value)
            return
        n = self.start
        while n != None:
            if n == None:
                print('value not found in linked list')
            elif n.value == node_value:
                old_next = n.next  #save the current pointer to the next node
                n.next = Node(value) #update the next pointer to be a new Node
                n.next.next = old_next #set the next pointer of the new node to be the previous next pointer in the current node
            n = n.next
    
    def insert_before(self,node_val,value):
        #find the node that matches with n.next.  
        #if the node_val matches, 
        print(f'insert {value} before {node_val}')
        n = self.start
        while n.next != None:
            print('current',n.value,'next', n.next.value)
            if n.next.value == node_val:
                old_n = n
                n = Node(value)
                n.next = old_n.next
                old_n.next = n
                print(f'inserted {n.value} before {n.next.value}')
            n = n.next


        # if self.start == None:
        #     self.start = Node(value)
        #     return
        # n = self.start
        # while n.next != None:

            

    def insert_at_end(self,value):
        new_node = Node(value)
        if self.start == None:
            self.start = new_node
            return
        n = self.start
        while n.next != None:
            n = n.next
        n.next = new_node


ll = LinkedList()
ll.insert_at_start(15)
ll.insert_at_start(20)
ll.insert_at_end(30)
ll.insert_after(20,22)
ll.insert_after(22,29)
ll.insert_before(29,1)
# ll.insert_before(22,17)
ll.print_list()


