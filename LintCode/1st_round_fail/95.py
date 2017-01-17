#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
	def isValidBSThelper(self, root, min_val, max_val):
		if root == None:
			return True
		if root.val > min_val and root.val < max_val:
			return self.isValidBSThelper(root.left, min_val, root.val) and self.isValidBSThelper(root.right, root.val, max)
		else:
			return False

	def isValidBST(self, root):
		min_val = -sys.maxint
		max_val = sys.maxint
		return self.isValidBSThelper(root, min_val, max_val)

if __name__ == '__main__':
   









