
# Binary Search Trees
# Should have the methods insert, contains, get_max.

# insert adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.

# contains searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.

# get_max returns the maximum value in the binary search tree.

# for_each performs a traversal of every node in the tree, executing the passed-in callback function on each tree node value. There is a myriad of ways to perform tree traversal; in this case any of them should work.

class Node:
    def __init__(self,val,up=None,left=None,right=None):
        self.value = val
        self.up = up
        self.left = left
        self.right = right
        self.printed = False
    
    def print(self):
        print("Node: ")
        print(dict([('value', self.value),('parent node:', self.up),('left child:', self.left),('right child', self.right)]))

# n = Node(50)
# n.print()

class BinarySearchTree:
    def __init__(self,initial_val):
        self.head = Node(initial_val)
        self.size = 0
        self.prints = 0
    
    def morris_traverse(self):
        print('printing entire tree, the morris way: ')
        # Morris Traversal
        # 1. Initialize current as root 
        # 2. While current is not NULL
        #    If the current does not have left child
        #       a) Print current’s data
        #       b) Go to the right, i.e., current = current->right
        #    Else
        #       a) Make current as the right child of the rightmost 
        #          node in current's left subtree
        #       b) Go to this left child, i.e., current = current->left

        n = self.head

        while n:
            if n.left is None:
                print(n.value)
                n = n.right
            else:  #if n.left exists
                # Find the inorder predecessor of current
                pre = n.left 
                while pre.right and pre.right != n:
                    pre = pre.right

                # Make current as right child of its inorder predecessor
                if pre.right is None:
                    pre.right = n
                    n = n.left

                # Revert the changes made in if part to restore the  
                # original tree i.e., fix the right child of predecessor
                else:  #pre.right is not None
                    pre.right = None
                    print(n.value)
                    n = n.right

    def insert(self,value):
        self.size = self.size + 1
        n = self.head
        # print('n', self.head.value, 'n.left', n.left, 'n.right', n.right)
        while n:
            # print('n.value', n.value, 'value', value, 'value < n.value ? ', value < n.value)
            if value > n.value:
                # print('value > n.value ? ', value, n.value, 'n.right', n.right)
                if not n.right:
                    n.right = Node(value)
                    n.right.up = n
                    n = n.right
                    break
                else:
                    n = n.right
                    # n.right.up = n
            elif value < n.value:
                # print('value < n.value ? ', value, n.value, value < n.value)
                if not n.left:
                    n.left = Node(value)
                    n.left.up = n
                    n = n.left
                    break
                else:
                    n = n.left
                    # n.left.up = n
        
        print('n.value', n.value)

    def contains(self):
        pass

    def get_max(self):
        pass

    def depth_traverse_in(self):
        print('time to traverse the tree in depth in order!')
        n = self.head
        # self.prints = 0 already initialized in the constructor

        # while n and self.prints <= self.size+5:
        while n:
            print('\nn',n.value)
            print('n.left', n.left)
            if n.left is not None: print(n.left.value) 
            print('n.right', n.right)
            if n.right: print(n.right.value) 
            print('\n')
           
            #case 1:
            if n.left and n.right:
                # print('n.printed', n.printed)
                # print('n.left.printed?', n.left.printed)
                # print('n.right.printed?', n.right.printed)

                # if n.printed == False:

                # if n.printed:
                #     if not n.up:
                #         break
                #     else:
                #         n = n.right
                #         print('n moved right')

                if n.left.printed and n.right.printed:
                    if n.up:
                        print('both left and right have been printed, n.value:')
                        print(n.value)
                        n.printed = True
                        self.prints = self.prints + 1
                        n = n.up
                        print('n moved up')
                    else: #no up
                        print('total prints: ', self.prints)
                        break  #exit condition from the while loop.  when left/right side is printed, and there is no up. ie. the root node
                elif n.left.printed: #only
                    print(n.value)
                    n.printed = True
                    self.prints = self.prints + 1
                    n = n.right
                    print('n moved to the right')

                else: #n.left not printed , n.right not printed
                    print('n moved to the lefty')
                    n = n.left

                # elif n.left.printed:
                #     if not n.up:
                #         print('left and right, but no up since its probably the head')
                #         print(n.value)
                #         n.printed = True
                #         self.prints = self.prints + 1
                #     else: #up exists
                #         if n.right.printed:
                #             print('both left and right have been printed, n.value:')
                #             print(n.value)
                #             n.printed = True
                #             self.prints = self.prints + 1
                #             n = n.up
                #             print('n moved up')
                #         else:
                #             n = n.right
                #             print('n moved to the right')
                # else: #n.left.printed == False
                #     print('n moved to the lefty')
                #     n = n.left

            #case 2:
            elif n.left and not n.right:
                if n.left.printed:
                    print('left but no right, n.value:')
                    print(n.value)
                    n.printed = True
                    self.prints = self.prints + 1
                    n = n.up
                    print('n moved up')
                else: #n.left.printed == False  # not n.left.printed
                    n = n.left
                    print('n moved to the left')

            #case 3:
            elif n.right and not n.left:

                if not n.printed:
                    print('there is right but no left n.value:')
                    print(n.value)
                    n.printed = True
                    self.prints = self.prints + 1
                    n = n.right
                    print('n moved right')
                else: #n.printed == True
                    print('there is right, no left, and n.printed is true', n.value)
                    n = n.up
                    print('n moved up')


                # if n.right.printed == False:
                #     n = n.right
                #     print('n moved to the right')
                
                # else: #n.right.printed == True
                #     print('right already printed, n.value:')
                #     print(n.value)
                #     n.printed = True
                #     self.prints = self.prints + 1
                #     n = n.up
                #     print('n moved up')
                
            #case 4:
            if not n.left and not n.right:
                print('no n.left nor n.right, n.value:')
                print(n.value)
                n.printed = True
                self.prints = self.prints + 1
                n = n.up
                print('n moved up')



    def depth_traverse_pre(self):
        print('time to traverse the tree pre-order style!!')
        pass

    def depth_traverse_post(self):
        print('time to traverse the tree post-order style!!')
        pass


    def for_each(self):
        t = input("What type of traversal? Choose a number: 1-depth or 2-breadth ")
        if t == '1':
            d = input("what type of depth order?  choose a number: 1-Pre,2-Post,3-In ")
            if d == '1':
                print('calling a preorder depth traversal')
                self.depth_traverse_pre()
            elif d =='2':
                print('calling a post-order depth traversal')
                self.depth_traverse_post()
            elif d=='3':
                print('calling an in-order depth traversal')
                self.depth_traverse_in()
            else:
                print('you did not select a valid type of depth traversal. running the in-order by default')
        elif t =='2':
            print('calling a breadth traversal')
        else: 
            print('you did not select a valid traversal selection. run the program again...')


tree = BinarySearchTree(5)
tree.insert(6)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(10)
tree.insert(4)
tree.insert(7)
tree.insert(8)
tree.insert(9)
# tree.morris_traverse()

# tree.morris_traverse()
tree.depth_traverse_in()


 # start at self.head. set n = self.head.  
        # check n.left and n.right:
            # case 1: if there's both n.left and n.right  (assumption: head of a tree will always have at leaset 1 left and right, so only account for that case when theres n.left and n.right)
                #if n itself is printed:
                    # go n.right
                #
                # if n.left.printed:
                    #if theres no n.up:
                        # print(n.value)
                        # set n.printed = True
                    # else: (there is a n.up)
                        # if n.right.printed:
                            #go to n.up
                        # else: go to n.right
                # else: (n.left is not printed)
                #   go n.left

            # case 2: if there's only n.left
                # if n.left.printed:
                    # print(n.value)
                    # mark this as n.printed
                    # go to n.up
                # else: go n.left
            # case 3: if there's only n.right
                # print(n.value)
                # go n.right
            # case 4: NO n.left NO n.right:
                # print(n.value)
                # mark as n.printed = True
                # go to n.up




        #travel until there is no n.left or n.right
            # case 1: both n.left and n.right are there.
            # case 2: n.left is there, but n.right is NOT.
            # case 3: 
        # for each node, printorder() will be :  n.left, n, n.right,
        #  then move back to n.  Then go to n.up.
        #  then check if there's a n.right.  
        # if there is go to it. 
        # check if there's a left and a right.  if there is,  then perform the minitreeprint()
        # if there's only a left: go to it and print it.  then go to the n.up and print that.
        # if there's only a right: print n.value, then go to n.right and print it.  then move up n.up twice.  
        # else: go to n.up




# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


# class BinarySearchTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     # Insert the given value into the tree
#     def insert(self, value):
#         pass

#     # Return True if the tree contains the value
#     # False if it does not
#     def contains(self, target):
#         pass

#     # Return the maximum value found in the tree
#     def get_max(self):
#         pass

#     # Call the function `cb` on the value of each node
#     # You may use a recursive or iterative approach
#     def for_each(self, cb):
#         pass

#     # DAY 2 Project -----------------------

#     # Print all the values in order from low to high
#     # Hint:  Use a recursive, depth first traversal
#     def in_order_print(self, node):
#         pass

#     # Print the value of every node, starting with the given node,
#     # in an iterative breadth first traversal
#     def bft_print(self, node):
#         pass

#     # Print the value of every node, starting with the given node,
#     # in an iterative depth first traversal
#     def dft_print(self, node):
#         pass

#     # STRETCH Goals -------------------------
#     # Note: Research may be required

#     # Print In-order recursive DFT
#     def pre_order_dft(self, node):
#         pass

#     # Print Post-order recursive DFT
#     def post_order_dft(self, node):
#         pass






                 

        # while n is not None:
        #     print('in the while loop')
        #     if n.left == None and n.right == None:
        #         if val > n.value:
        #             n.right = Node(val)
        #             n.right.up = n
        #             # n = n.right
        #         else:  #val < n.value
        #             n.left = Node(val)
        #             n.left.up = n
        #             # n = n.left
        #     # else: #n.left exists or n.right exists or BOTH exist
        #     elif n.right and not n.left:
        #         n = n.right
        #     else:  #n.left and not n.right
        #         n = n.left
        
        # print('n', n.value)

        # if val > n.value:
        #     print('right!!!')
        #     n.right = Node(val)
        #     n.right.up = n

        # if val < n.value:
        #     print('left!!!')
        #     print('n.left in val < n.value', n.left)
        #     n.left = Node(val)
        #     n.left.up = n

        




        # print('val to insert', val, 'n.value', n.value, 'n.left', n.left, 'n.right', n.right)
        
        # while n.left != None or n.right != None:
        #     if val > n.value:
        #             n = n.right
            
        #     if val < n.value:
        #             n = n.left

        # print('n value after traversal', n.value, 'n.left', n.left, 'n.right', n.right)

        # if val > n.value:
        #     print('right!!!')
        #     n.right = Node(val)
        #     n.right.up = n

        # if val < n.value:
        #     print('left!!!')
        #     print('n.left in val < n.value', n.left)
        #     n.left = Node(val)
        #     n.left.up = n


        #start at n = self.head
        #compare values till you get to end.  THEN compare as below:
        #if val > head, n.right = val
        #if val < head, n.left = val
        # n.left.up or n.right.up = n
        # head = n.head

        # val = value to insert
        # while you can go left or right
        # compare val to node value
        #     if val > node val : shift to right node and repeat while loop
        #     if val < node val : shift to left node and repeat while loop
        # after while loop, you re at the end node.
        # compare to 