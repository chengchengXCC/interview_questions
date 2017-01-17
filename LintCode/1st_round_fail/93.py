#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
	def absOfDiff(self, a, b):
		if a >= b:
			return a - b
		else:
			return b - a
    '''
    # Sol1
    def isBalanced(self, root):
    	if root == None:
    		return True
    	lH = self.maxDepth(root.left)
    	rH = self.maxDepth(root.right)
    	if self.absOfDiff(lH, rH) > 1:
    		return False
    	else:
    		return self.isBalanced(root.left) and self.isBalanced(root.right)
    '''
    # Sol2
    def isBalancedhelper(self, root):
    	if root == None:
    		return 0
    	lH = self.isBalancedhelper(root.left)
    	lH = self.isBalancedhelper(root.right)
    	if lH == -1 or rH == -1 or self.absOfDiff(lH, rH) > 1:
    		return -1
    	return max(lH, rH) + 1

    def isBalanced(self, root):
    	return self.isBalancedhelper(root) != -1

if __name__ == '__main__':
    s = Solution()
    #pdb.set_trace()
    print s.permuteUnique([1,2,2])









