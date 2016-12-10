#!/usr/bin/python
import requests
import pdb
import sys

"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""

class Solution:
	def findPath(self, root, node):
		result = []
		while node != root:
			result.append(node)
			node = node.parent
		return result
		
	def lowestCommonAncestorII(self, root, A, B):
		# get two paths
		# path1: root to A
		# path2: root to B
		# find the last common node, and return it
		path1 = self.findPath(root, A)
		path2 = self.findPath(root, B)
		path1.reverse()
		path2.reverse()
		node = None
		for i in range(0, len(path1)):
			if path1[i] == path2[i]:
				node = path1[i]
			else:
				break
		return node
		