#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
	# Sol1: DFS
    '''
    def helper(self, root, result):
        if root == None:
            return
        self.helper(root.left, result)
        self.helper(root.right, result)
        result.append(root.val)

    def postorderTraversal(self, root):
        result = []
        if root == None:
            return result
        self.helper(root, result)
        return result
    '''
   
    # Sol2: D & C
    
    def postorderTraversal(self, root):
        result = []
        if root == None:
            return result
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return left + right + [root.val]
    

