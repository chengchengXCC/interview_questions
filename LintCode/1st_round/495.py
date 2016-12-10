class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []

    # @param x, an integer, push a new item into the stack
    # @return nothing
    def push(self, x):
        # Write your code here
        self.stack.append(x)
        
    # @return nothing, pop the top of the stack
    def pop(self):
        # Write your code here
        self.stack.pop()

    # @return an integer, return the top of the stack
    def top(self):
        # Write your code here
        return self.stack[len(self.stack) - 1]

    # @return a boolean, check the stack is empty or not.
    def isEmpty(self):
        # Write your code here
        return len(self.stack) == 0