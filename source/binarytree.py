#!python

from collections import deque


class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # Check if both left child and right child have no value
        return self.left is None and self.right is None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # Check if either left child or right child has a value
        return self.left is not None or self.right is not None

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        Best case running time:???
        Worst case running time:???"""
        if self.is_leaf():
            return 0
        left_height = 0
        if self.left is not None:
            left_height = self.left.height()
        right_height = 0
        if self.right is not None:
            right_height = self.right.height()
        return 1 + max(left_height, right_height)


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        Best case running time: ???
        Worst case running time: ???"""

        if self.root is not None:
            return self.root.height()

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node(item)
        # Return true  node was found, none if not
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node(item)
        # ReturnNone if not found and node data it it is
        return node.data if node is not None else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # if tree is empty
        if self.is_empty():
            self.root = BinaryTreeNode(item)
            #increment
            self.size += 1
            return
        # Find parent node where item is going to be put
        parent = self._find_parent_node(item)
        #  if item should be put to the left node
        if item < parent.data:
            # Create node and set the parent left child
            parent.left = BinaryTreeNode(item)
        # if item should be put to the left node
        elif item > parent.data:
            # new node and set the parent's right child
            parent.right = BinaryTreeNode(item)
        # Increment the tree size
        self.size += 1

    def _find_node(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        node = self.root
        # while loop we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node data value
            if item == node.data:
                # Return the found node
                return node
            # if the item is less than the node data value
            elif item < node.data:
                # go to  the node left child
                node = node.left
            #  if the item ismore than the node data value
            elif item > node.data:
                # go to nod right child
                node = node.right
        # if node is not found
        return None

    def _find_parent_node(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        node = self.root
        parent = None
        while node is not None:
            if item == node.data:
                return parent
            elif item < node.data:
                parent = node
                node = node.left
            elif item > node.data:
                parent = node
                node = node.right
        # Not found
        return parent

    # This space intentionally left blank (please do not delete this comment)
    #WHAT IF I DO ALAN????

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in order from root to leaf, appending each node'sdata value
            self._traverse_in_order_recursive(self.root, items.append)
        # Return  list of data values in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # , if it exists, traverse left sub-tree
        if node.left is not None:
            self._traverse_in_order_recursive(node.left, visit)
        # Visit function with node data as parameter
        visit(node.data)
        #  if it exists ttraverse right sub-tree
        if node.right is not None:
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse in-order without using recursion (stretch challenge)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree  from root, appending each node's data value to list to be returned
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return  list of all values in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # Visit function with node data as parameter
        visit(node.data)
        # , if it exists traerse left subtree
        if node.left is not None:
            self._traverse_pre_order_recursive(node.left, visit)
        #  if it exists,traverse right subtree
        if node.right is not None:
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        #if it exists, traverse the node'sleft sub-tree
        if node.left is not None:
            self._traverse_post_order_recursive(node.left, visit)
        # if it exists,travese the nodes right sub-tree
        if node.right is not None:
            self._traverse_post_order_recursive(node.right, visit)
        # Visitfunction, node data value
        visit(node.data)

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse post-order without using recursion (stretch challenge)
        #if node.

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        # empty list that will be returned with items
        items = []
        if not self.is_empty():
            # Traverse tree level from root node while appending each node value
            self._traverse_level_order_iterative(self.root, items.append)
        # return list pf items
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n) Why and under what conditions?
        TODO: Memory usage: O(n) Why and under what conditions?"""
        # Create queue for traversal
        queue = deque()
        # append starting node
        queue.append(start_node)
        #  until queue is empty and nothing left
        while len(queue) > 0:
            # Dequeue node in front
            node = queue.popleft()
            # this node data value with  function
            visit(node.data)
            #  if it exists, enqueue  nodeleft child
            if node.left is not None:
                queue.append(node.left)
            # same as last but on right
            if node.right is not None:
                queue.append(node.right)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
