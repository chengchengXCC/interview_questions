#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
	def leftMost(self, root):
		tmp = root
		while tmp.left:
			tmp = tmp.left
		return tmp

	def rightMost(self, root):
		tmp = root
		while tmp.right:
			tmp = tmp.right
		return tmp

	def removeNode(self, root, value):
		prev = None
		tmp = root
		# locate target node
		while tmp and tmp.val != value:
			prev = tmp
			if tmp.val > value:
				tmp = tmp.left
			else:
				tmp = tmp.right
		# if target node is not found
		if tmp.val != value:
			return
		# if target node is root
		if parent == None:
			if tmp.left:
				self.rightMost(tmp.left).right = tmp.right
				return tmp.left
			elif tmp.right:
				self.leftMost(tmp.right).left = tmp.left
				return tmp.right
			else:
				return None
		# if target node is not root
		if tmp.left:
			self.rightMost(tmp.left).right = tmp.right
			if parent.left == tmp:
				parent.left = tmp.left
			else:
				parent.right = tmp.left
		elif tmp.right:
			self.leftMost(tmp.right).left = tmp.left
			if parent.left == tmp:
				parent.left = tmp.right
			else:
				parent.right = tmp.right
		else:
			tmp = None
		return root

if __name__ == '__main__':
   









