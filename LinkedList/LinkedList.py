# A linked list is a data structure type that allows data to be dynamically created easily versus memory

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class DENode(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

# Queue is FIFO
class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        node = Node(val)

        node.next = None

        if not self.head and not self.tail:
            self.head = self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def dequeue(self):
        temp = self.head

        if self.head:
            self.head = self.head.next

        if temp:
            return temp.val
        else:
            return None

# Stack is FILO
class Stack(object):
    def __init__(self):
        self.top = None

    def push(self, val):
        node = Node(val)

        node.next = self.top
        self.top = node

    def pop(self):
        temp = self.top

        self.top = self.top.next

        return temp.val
