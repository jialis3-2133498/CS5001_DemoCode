class Queue:
    """a queue class using a Python
    list as its implementation"""
    def __init__(self):
        self.items = []

    def __str__(self):
        # what is __str__?
        return str(self.items)

    def enqueue(self, item):
        # Insert the element into the list
        self.items.insert(0, item)

    def dequeue(self):
        # it takes out the element in the same order like enqueue
        return self.items.pop()
        # pop() build-in

    def peek(self):
        # Check the next item in the queue
        return self.items[-1]

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
