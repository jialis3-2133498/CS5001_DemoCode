class Stack:
    """A simple stack for enabling undo for 
    spot placement"""
    def __init__(self):
        self.contents = []
        
    def push(self, item):
        self.contents.append(item)

    def pop(self):
        if len(self.contents) > 0:
            return self.contents.pop()
