#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # Check if empty
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this queue."""
        # Count number of items
        return self.list.length()

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – The append doesnt need to iterate through
        all nodes since its a list it and just adds to the back """
        # Insert given item
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # Return front item, if any
        if self.is_empty():
            return None
        return self.list.head.data

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) – first item is just empty so noeiterations needed"""
        # Remove and return front item, if any
        if self.is_empty():
            raise ValueError('Cannot dequeue on an empty queue')

        front = self.list.head.data
        self.list.delete(front)
        return front


# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # Check if empty
        return self.length() == 0

    def length(self):
        """Return the number of items in this queue."""
        # Count number of items
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – The run time is o(1). sine the big o for the list at appent is o(1) due to not have to iterate"""
        # Insert given item
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # Return front item, if any
        if self.is_empty():
            return None
        return self.list[0]

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(n) due to having to shift all the other elements back to fill space """
        # Remove and return front item, if any
        if self.is_empty():
            raise ValueError('Cannot pop on an empty stack')
        return self.list.pop(0)


#estting
# Queue = LinkedQueue
Queue = ArrayQueue
