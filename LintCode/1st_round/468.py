#!/usr/bin/python

import requests
import pdb
import sys
import Queue

class Solution:
	# method1: recursive
	'''
	def helper(self, root1, root2):
		if root1 == None and root2 == None:
			return True
		if root1 == None or root2 == None:
			return False
		if root1.val != root2.val:
			return False
		return self.helper(root1.left, root2.right) and self.helper(root1.right, root2.left)

	def isSymmetric(self, root):
		if root == None:
			return True
		return self.helper(root.left, root.right)
	'''
	# method2: iterative
	def getH(self, root):
		if root == None:
			return 0
		lH = self.getH(root.left)
		rH = self.getH(root.right)
		return max(lH, rH) + 1

	def helper(self, root, result, i):
		if root == None:
			result[i].append('#')
			return
		result[i].append(root.val)
		self.helper(root.left, result, i + 1)
		self.helper(root.right, result, i + 1)

	def isPalindrome(self, s):
		i = 0
		j = len(s) - 1
		while i < j:
			if s[i] != s[j]:
				return False
			i += 1
			j -= 1
		return True

	def isSymmetric(self, root):
		if root == None:
			return True
		h = self.getH(root)
		result = []
		for i in range(0, h):
			result.append([])
		self.helper(root, result, 0)
		for i in range(0, h):
			if not self.isPalindrome(result[i]):
				return False
		return True

if __name__ == '__main__':
   









