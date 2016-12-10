#!/usr/bin/python

import requests
import pdb
import sys
import Queue

class Solution:
	def getHeight(self, root):
		if root == None:
			return 0
		lH = self.getHeight(root.left)
		rH = self.getHeight(root.right)
		return max(lH, rH) + 1

	# method 1: 2 Queues
	'''
	def levelOrder(self, root):
		result = []
		if root == None:
			return result
		q1 = Queue.Queue()
		q2 = Queue.Queue()
		q1.put(root)
		while q1:
			level = []
			while q1:
				tmp = q1.get()
				q2.put(tmp)
				level.append(tmp.val)
			while q2:
				tmp = q2.get()
				q1.put(tmp)
			result.append(level)
		return result
	'''
	# method 2: 1 Queue
	'''
	def levelOrder(self, root):
		result = []
		if root == None:
			return result
		q = Queue.Queue()
		q.put(root)
		while not q.empty():
			n = len(q)
			level = []
			for i in range(0, n):
				tmp = q.get()
				level.append(tmp.val)
				if tmp.left:
					q.put(tmp.left)
				if tmp.right:
					q.put(tmp.right)
			result.append(level)
		return result
	'''
	# method 3: DFS
	def dfs_helper(self, root, i, result):
		if root == None:
			return
		result[i].append(root.val)
		self.dfs_helper(root.left, i + 1, result)
		self.dfs_helper(root.right, i + 1, result)

	def levelOrder(self, root):
		result = []
		if root == None:
			return result
		n = self.getHeight(root)
		for i in range(0, n):
			result.append([])
		self.dfs_helper(root, 0, result)
		return result

if __name__ == '__main__':
   









