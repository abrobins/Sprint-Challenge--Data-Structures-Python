"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from queue import Queue
from stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take current value of our node (self.value)
        # compare to the new value we want to insert
        # think of base case where we don't need to recurse (here it's if self.left is None / self.left = BSTNode(value) and the right side as well)
        if value < self.value:  # compare value being passed in to node value
            if self.left is None:
                self.left = BSTNode(value)
            else:
                # if self.left is already taken by a node
                # make that node call insert - recursion
                # repeat function insert in this case until we reach base case
                self.left.insert(value)

        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:  # base case
            return True
        # which direction are we moving?
        if self.value > target:
            if self.left is None:
                return False
            found = self.left.contains(target)
        else:
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found

        # if current self.value  == target
        # return True
        # compare target to current value
        # if current value < target
        # check left subtree (self.left.contains(target))
        # if you cannot go left, return False
    # if current value >= target
        # check if right subtree contains target
        # if you cannot go right, return False

    # Return the maximum value found in the tree

    def get_max(self):
        current = self
        while (current.right):
            current = current.right
        return current.value

        # other way to do this:
        # if self.right is None:
        #   return self.value
        # else:
        #   return self.right.get_max()

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # lowest number always furthest on left

        # need base case
        if node is None:
            return
        else:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

            # need recursive case (gets us closer to base case)

        # what if node is none?

        # build up call stack to see what happens (builds up then tears down)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # queue because coming off line by line
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)

        while queue.len() > 0:
            node = queue.dequeue()
            print(node.value)
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)
        # not using recusion
        # use a queue

        # start queue with root node

        # use while loop (condition while queue is not empty)
        # check size of queue
        # remove first node from the queue
        # print that removed node
        # add all children into queue
        # repeat
        # have some sort of pointer variable that updates at beginning of each loop

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        # use a stack class
        # you can mimic recusion with stack data structure
        # start your stack with the root node

        stack = Stack()
        stack.push(node)
        while stack.len() > 0:
            node = stack.pop()
            print(node.value)
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)

        # use while loop that checks size of stack and while not empty
        # get current node from top of stack and print it
        # add all children to the stack because you won't have access to them later
        # keep in mind, order you add children matters

        # use pointer

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
