#!/usr/bin/python

import requests
import pdb
import sys
import Queue

class Solution:
	def minDepth_helper(self, root):
		if root.left == None and root.right == None:
			return 1
		if root.left == None:
			lH = sys.maxint
			rH = self.minDepth_helper(root.right)
		elif root.right == None:
			lH = self.minDepth_helper(root.left)
			rH = sys.maxint
		else:
			lH = self.minDepth_helper(root.left)
			rH = self.minDepth_helper(root.right)
		return min(lH, rH) + 1

	def minDepth(self, root):
		if root == None:
			return 0
		return self.minDepth_helper(root)
		
