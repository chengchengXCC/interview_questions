#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
	def helper(self, root, k1, k2, result):
		if root == None:
			return
		self.helper(root.left, k1, k2, result)
		if root.val >= k1 and root.val <= k2:
			result.append(root)
		self.helper(root.right, k1, k, result)

	def searchRange(self, root, k1, k2):
		result = []
		self.helper(root, k1, k2, result)
		return result

if __name__ == '__main__':
   









