class ThreeStacks:
    # @param {int} size, the size of each stacks
    def __init__(self, size):
        # initialize your data structure here.
        self.array = [None for i in range(3 * size)]
        self.size = [0 for i in range(3)]
        self.maxSize = size

    # @param {int} stack_num an integer
    # @param {int} value an integer
    # @return nothing
    def push(self, stack_num, value):
        # Write your code here
        # Push value into stack_num stack
        index = stack_num * self.maxSize + self.size[stack_num]
        self.array[index] = value
        self.size[stack_num] += 1

    # @param {int} stack_num an integer
    # @return an integer
    def pop(self, stack_num):
        # Write your code here
        # Pop and return the top element from stack_num stack
        index = stack_num * self.maxSize + self.size[stack_num] - 1
        result = self.array[index]
        self.array[index] = None
        self.size[stack_num] -= 1
        return result

    # @param {int} stack_num an integer
    # @return an integer
    def peek(self, stack_num):
        # Write your code here
        # Return the top element
        index = stack_num * self.maxSize + self.size[stack_num] - 1
        return self.array[index]

    # @param {int} stack_num an integer
    # @return a boolean
    def isEmpty(self, stack_num):
        # Write your code here
        return self.size[stack_num] == 0
