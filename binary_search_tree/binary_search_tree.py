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
  
            node.in_order_print(node.left)
    
            print(node.value)
    
            node.in_order_print(node.right)
        # print('\n')
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(self)
        while q.len() > 0:
            node_current = q.dequeue()
            print(node_current.value)
            if node_current.left:
                q.enqueue(node_current.left)
            if node_current.right:
                q.enqueue(node_current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        st = Stack()
        st.push(self)
        while st.len() > 0:
            node_current = st.pop()
            print(node_current.value)
            if node_current.left:
                st.push(node_current.left)
            if node_current.right:
                st.push(node_current.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(self.value)
        if self.left:
            self.left.pre_order_dft(self.left)
        if self.right:
            self.right.pre_order_dft(self.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node=None):
        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)

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