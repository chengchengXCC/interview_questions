#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
	def helper(self, root):
		if root == None:
			return 0, -sys.maxint
		left = self.helper(root.left)
		right = self.helper(root.right)
		singlePath = max(0, max(left[0], right[0]) + root.val)
		maxPath = max(max(left[1], right[1]), left[0] + right[0] + root.val)
		return singlePath, maxPath

	def maxPathSum(self, root):
		singlePath, maxPath = self.helper(root)
		return maxPath 
    	
if __name__ == '__main__':
   









