'''
class MinStack(object):
    def __init__(self):
        # do some intialize if necessary
        self.stack = []
        self.min_v = sys.maxint

    def push(self, number):
        # write yout code here
        self.stack.append(number)
        self.min_v = min(self.min_v, number)

    def pop(self):
        # pop and return the top item in stack
        result = self.stack.pop()
        self.min_v = sys.maxint
        for i in range(0, len(self.stack)):
            self.min_v = min(self.min_v, self.stack[i])
        return result
        
    def min(self):
        # return the minimum number in stack
        return self.min_v
'''
class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.stack = []
        self.min_stack = []

    def push(self, number):
        # write yout code here
        self.stack.append(number)
        if len(self.min_stack) == 0:
            self.min_stack.append(number)
        else:
            if number <= self.min_stack[len(self.min_stack) - 1]:
                self.min_stack.append(number)

    def pop(self):
        # pop and return the top item in stack
        result = self.stack.pop()
        if result == self.min_stack[len(self.min_stack) - 1]:
            self.min_stack.pop()
        return result
        
    def min(self):
        # return the minimum number in stack
        return self.min_stack[len(self.min_stack) - 1]


       

                
                
                
                    