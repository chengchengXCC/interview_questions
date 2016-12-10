class Stack(object):
    def __init__(self):
        self.stack = []
        
    def push(self, number):
        self.stack.append(number)
        
    def pop(self):
        num = self.stack.pop()
        return num
    
    def top(self):
        return self.stack[len(self.stack) - 1]
            
    def isEmpty(self):
        return len(self.stack) == 0

class Solution:
    def largestRectangleArea(self, height):
    	if height == None or len(height) == 0:
    		return 0
    	stack = Stack()
    	maxArea = 0
    	for i in range(0, len(height) + 1):
    		if i == len(height):
    			curt = -1
    		else:
    			curt = height[i]
    		while not stack.isEmpty() and curt <= stack.peek():
    			h = stack.pop()
    			if stack.isEmpty():
    				w = i
    			else:
    				w = i - stack.peek() - 1
    			maxArea = max(maxArea, w * h)
    		stack.push(i)
    	return maxArea






       