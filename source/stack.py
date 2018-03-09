#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # Check if empty
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this stack."""
        # Count number of items
        return self.list.length()

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – The run time is constant regardless of the number
        of nodes in the linked list. A new node is created and prepended to the
        beginning of the linked list; nothing is iterated through."""
        # Push given item
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # Return top item, if any
        if self.is_empty():
            return None
        # return self.list.get_at_index(0)
        # Getting head.data is slightly faster and makes more sense to call
        return self.list.head.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – The run time is constant. Even through the stack
        can get really big, all the methods that are run are done on the first
        item in the stack."""
        # Remove and return top item, if any
        if self.is_empty():
            raise ValueError('Cannot pop on an empty stack')

        peek = self.list.head.data
        self.list.delete(peek)
        return peek

# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # Check if empty
        return self.length() == 0

    def length(self):
        """Return the number of items in this stack."""
        # Count number of items
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – The run time is constant. The built in append
        method for lists is O(1), probably because one calculation needs to be
        done in order to find the end of the list. Rarely, if the array fills
        up, the run time is longer (O(n)) because a bigger array must be
        created and the items must be copied over."""
        # Insert given item
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # Return top item, if any
        if self.is_empty():
            return None
        return self.list[-1]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – The run time is constant. The built in pop method
        for lists is O(1) if the last item in the list is popped. Like the
        append method, this is probably because one calculation needs to be
        done in order to find the last item of the list."""
        # Remove and return top item, if any
        if self.is_empty():
            raise ValueError('Cannot pop on an empty stack')
        return self.list.pop()

# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack
