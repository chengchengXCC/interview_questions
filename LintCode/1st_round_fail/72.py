#!/usr/bin/python

import requests
import pdb
import sys
import Queue

class Solution:
	def buildTree_helper(self, inorder, postorder):
		if len(inorder) == 0:
			return None
		if len(inorder) == 1:
		    return TreeNode(inorder[-1])
		val = postorder[-1]
		root = TreeNode(val)
		inorder_left = inorder[0:inorder.index(val)]
		inorder_right = inorder[inorder.index(val)+1:len(inorder)]
		postorder_left = postorder[0:len(inorder_left)]
		postorder_right = postorder[len(inorder_left):len(postorder)-1]
		root.left = self.buildTree_helper(inorder_left, postorder_left)
		root.right = self.buildTree_helper(inorder_right, postorder_right)
		return root

	def buildTree(self, inorder, postorder):
		if inorder == None or len(inorder) == 0:
			return None
		return self.buildTree_helper(inorder, postorder)