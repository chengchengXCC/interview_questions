#!/usr/bin/python

import requests
import pdb
import sys
import Queue

class Solution:
	def getH(self, root):
		if root == None:
			return 0
		lH = self.getH(root.left)
		rH = self.getH(root.right)
		return max(lH, rH) + 1
	'''
	def helper(self, root, result, i):
		if root == None:
			if i < len(result):
				result[i].append('#')
			return
		result[i].append(root.val)
		self.helper(root.left, result, i + 1)
		self.helper(root.right, result, i + 1)

	def isComplete_helper(self, result, h):
		for i in range(0, h):
			if i != h - 1 and '#' in result[i]:
				return False
			if i == h - 1:
				for j in range(0, len(result[i]) - 1):
					if result[i][j] == '#' and result[i][j + 1] != '#':
						return False
		return True

	def isComplete(self, root):
		if root == None:
			return True
		h = self.getH(root)
		result = []
		for i in range(0, h):
			result.append([])
		self.helper(root, result, 0)
		return self.isComplete_helper(result, h)
	'''

	def isComplete(self, root):
		if root == None:
			return True
		h = self.getH(root)
		q = Queue.Queue()
		q.put(root)
		i = 1
		while not q.empty():
			n = q.qsize()
			prev = None
			for j in range(0, n):
				tmp = q.get()
				if i != h and tmp.val == '#':
					return False
				if i == h and prev:
					if prev.val == '#' and tmp.val != '#':
						return False
				prev = tmp
				if tmp.left:
					q.put(tmp.left)
				if tmp.right:
					q.put(tmp.right)
			i += 1
		return True

if __name__ == '__main__':
   









