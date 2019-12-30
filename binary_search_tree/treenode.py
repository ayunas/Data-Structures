class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
    def __repr__(self):
        return repr(self.val)

def pre_order_traverse(root):
    if root is None:
        return
    print(root.val)
    pre_order_traverse(root.left)
    pre_order_traverse(root.right)

def post_order_traverse(root):
    if root is None:
        return
    post_order_traverse(root.left)
    post_order_traverse(root.right)
    print(root.val)

def in_order_traverse(root):
    if root is None:
        return
    in_order_traverse(root.left)
    print(root.val)
    in_order_traverse(root.right)


n = TreeNode(5)
n.left = TreeNode(3)
n.left.left = TreeNode(1)
n.right = TreeNode(8)
n.right.right = TreeNode(10)

pre_order_traverse(n)
print('\n')
post_order_traverse(n)
print('\n')
in_order_traverse(n)




