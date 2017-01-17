class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        tmp = self.stack[len(self.stack) - 1]
        self.stack.pop()
        return tmp
    def peek(self):
        tmp = self.stack[len(self.stack) - 1]
        return tmp
    def isEmpty(self):
        return self.stack.isEmpty()

class MyQueue:
    def __init__(self):
        self.stk1 = Stack()
        self.stk2 = Stack()

    def push(self, x):
        # write your code here
        if not self.stk1.isEmpty():
            while not self.stk1.isEmpty():
                self.stk2.push(self.stk1.pop())
            self.stk2.push(x)
        else:
            self.stk2.push(x)

    def top(self):
        # return the top element
        tmp = 0
        if not self.stk1.isEmpty():
            while not self.stk1.isEmpty():
                self.stk2.push(self.stk1.pop())
            tmp = self.stk2.peek()
        else:
            tmp = self.stk2.peek()
        return tmp

    def pop(self):
        # pop and return the top element
        tmp = 0
        if not self.stk1.isEmpty():
            while not self.stk1.isEmpty():
                self.stk2.push(self.stk1.pop())
            tmp = self.stk2.pop()
        else:
            tmp = self.stk2.pop()
        return tmp

if __name__ == '__main__':
    s = MyQueue()
    s.stk1.push(1)
    s.stk2.push(2)
    print s.stk1.pop()
    print s.stk2.pop()
