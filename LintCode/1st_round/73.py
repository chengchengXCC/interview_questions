#!/usr/bin/python

import requests
import pdb
import sys
import Queue

class Solution:
	def buildTree_helper(self, preorder, inorder):
		if len(inorder) == 0 :
			return None
		if len(inorder) == 1:
		    return TreeNode(inorder[-1])
		val = preorder[0]
		root = TreeNode(val)
		inorder_left = inorder[0:inorder.index(val)]
		inorder_right = inorder[inorder.index(val)+1:len(inorder)]
		preorder_left = preorder[1:1+len(inorder_left)]
		preorder_right = preorder[1+len(inorder_left):len(preorder)]
		root.left = self.buildTree_helper(preorder_left, inorder_left)
		root.right = self.buildTree_helper(preorder_right, inorder_right)
		return root

	def buildTree(self, preorder, inorder):
		if inorder == None or len(inorder) == 0:
			return None
		return self.buildTree_helper(preorder, inorder)