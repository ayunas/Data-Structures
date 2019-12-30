class Node:
    def __init__(self,val,left=None,right=None):
        self.value = val
        self.left = left
        self.right = right

    def __repr__(self):
        space = " "
        if self.left or self.right:
            space = "    "
        return f'  {self.value} \n /  \ \n{self.left}{space}{self.right}'

class BST:
    def __init__(self, val=None):
        self.root = None
    
    def set_root(self,val,left=None,right=None):
        left = Node(left)
        right = Node(right)
        self.root = Node(val,left,right)
    
    def get_root(self):
        return self.root
    
    def insert(self,root,val):
        if root is None:
            root = Node(val)
        else:
            if root.value > val:
                if root.left is None:
                    root.left = Node(val)
                else:
                    self.insert(root.left,val)
            else:
                if root.right is None:
                    root.right = Node(val)
                else:
                    self.insert(root.right,val)

    
    def in_order_traverse(self,node=None):
        "LEFT -> RIGHT -> ROOT"
        if node is None:
            return
        self.in_order_traverse(node.left)
        print(node.value)
        self.in_order_traverse(node.right)
    
    def pre_order_traverse(self,node=None):
        "ROOT -> LEFT -> RIGHT"
        if node is None:
            return
        print(node.value)
        self.pre_order_traverse(node.left)
        self.pre_order_traverse(node.right)
    
    def post_order_traverse(self,node=None):
        "LEFT -> RIGHT -> ROOT"
        if node is None:
            return
        self.pre_order_traverse(node.left)
        self.pre_order_traverse(node.right)
        print(node.value)
    
    def traverse(self):
        inp = input('1 for in-order, 2 for pre-order, 3 for post-order: ')
        if inp == '1':
            self.in_order_traverse(self.root)
            return
        if inp == '2':
            self.pre_order_traverse(self.root)
            return
        if inp == '3':
            self.post_order_traverse(self.root)
            return
        else:
            print('invalid entry. please rerun the program and try again ')
            return

    def __repr__(self):
        return repr(self.root)

tree = BST()
tree.set_root(10,5,20)
root = tree.get_root()
tree.insert(root,100)
tree.traverse()