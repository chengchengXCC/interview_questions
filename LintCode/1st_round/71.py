#!/usr/bin/python

import requests
import pdb
import sys
import Queue

class Solution:
	"""
	@param root: The root of binary tree.
	@return: A list of list of integer include 
			 the zig zag level order traversal of its nodes' values
	"""
	def getHeight(self, root):
		if root == None:
			return 0
		lH = self.getHeight(root.left)
		rH = self.getHeight(root.right)
		return max(lH, rH) + 1
		
	def dfs_helper(self, root, i, result):
		if root == None:
			return
		result[i].append(root.val)
		self.dfs_helper(root.left, i + 1, result)
		self.dfs_helper(root.right, i + 1, result)

	def zigzagLevelOrder(self, root):
		result = []
		if root == None:
			return result
		n = self.getHeight(root)
		for i in range(0, n):
			result.append([])
		self.dfs_helper(root, 0, result)
		for i in range(0, len(result)):
		if i % 2 == 1:
			result[i].reverse()
		return result
		