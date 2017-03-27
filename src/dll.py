"""Implementation of a double linked list in Python."""


class Node(object):
    """Node class for data storage."""

    def __init__(self, data=None, next_node=None, prev=None):
        """Initialize Node."""
        self.data = data
        self.next = next_node
        self.prev = prev


class DoubleLinkedList(object):
    """Double linked list impplementation.

    Methods supported
    push(val) - will insert the value ‘val’ at the head of the list
    append(val) - will append the value ‘val’ at the tail of the list
    pop() - will pop the first val off the head of the list and return it.
    shift() - will remove the last val from the tail of the list and return it.
    remove(val) - will remove the first instance of ‘val’ found in the list,
    starting from the head.
    """

    def __init__(self, data=None, head=None, tail=None):
        """Initialize list."""
        self.head = head
        self.tail = tail
        self._length = 0
        try:
            for val in data:
                self.push(val)
        except TypeError:
            if data:
                self.push(data)

    def push(self, val):
        """Add val to the head of the list."""
        old_head = self.head
        self.head = Node(val, old_head)
        if old_head:
            old_head.prev = self.head
        if not self.tail:
            self.tail = self.head
        self._length += 1

    def pop(self):
        """Remove the val from the head of the list."""
        to_return = self.head
        if self._length < 1:
            raise IndexError('Cannot pop from an empty list.')
        elif self._length is 1:
            self.head, self.tail = None, None
        else:
            self.head.next.prev, self.head = None, self.head.next
        self._length -= 1
        return to_return

    def append(self, val):
        """Add val to the tail of the list."""
        old_tail = self.tail
        self.tail = Node(val, None, old_tail)
        if old_tail:
            old_tail.prev = self.tail
        if not self.head:
            self.head = self.tail
        self._length += 1