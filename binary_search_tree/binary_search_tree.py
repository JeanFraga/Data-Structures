import sys
sys.path.append('../GitHub/Data-Structures/queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.dll_stack = Stack()
        self.dll_queue = Queue()
    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            self.value = value
            # return self.value
        else:
            if value < self.value:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)
            else:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if self.value is None:
        #     return False
        # if self.value == target:
        #     return True
        # else:
        #     if target < self.value:
        #         return self.left.contains(target)
        #     else:
        #         return self.right.contains(target)
        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        else:
            return True
    # Return the maximum value found in the tree
    def get_max(self):
        if self.value == None:
            return None
        # maxvalue = self.value
        if self.right == None:
            if self.left != None:
                return self.left.get_max()
        if self.right != None:
            return self.right.get_max()
        return self.value
        
        # else:
        #     self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)
                

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):
        # if node == None:
        #     node = BinarySearchTree()
        # if node.value == None:
        #     return None
        # node.dll_stack.push(node.value)
        # if node.left != None:
        #     while node.left != None:
        #         node.in_order_print(node)
        #     print(node.value)
        #     node.dll_stack.pop()
        # print(node.dll_stack.tail)
        # node.dll_stack.pop()
        if node: 
  
            # First recur on left child 
            node.in_order_print(node.left)
    
            # then print the data of node 
            print(node.value)
    
            # now recur on right child 
            node.in_order_print(node.right)
        # print('\n')
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if node: 
    
            # First recur on left child 
            printPostorder(nodeleft) 
    
            # the recur on right child 
            printPostorder(node.right) 
    
            # now print the data of node 
            print(node.val), 

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

# import sys
# sys.path.append('../GitHub/Data-Structures/binary_search_tree')
# from binary_search_tree import BinarySearchTree

# bst = BinarySearchTree(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.in_order_print(bst)