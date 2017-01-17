#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
    def insertNode(self, root, node):
		parent = None
		tmp = root
		while tmp:
			parent = tmp
			if tmp.val > node.val:
				tmp = tmp.left
			else:
				tmp = tmp.right
		if parent == None:
			return TreeNode(node.val)
		if parent.val > node.val:
			parent.left = TreeNode(node.val)
		else:
			parent.right = TreeNode(node.val)
		return root


if __name__ == '__main__':
   









