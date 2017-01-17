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
        result.append(root.val)
        self.helper(root.right, result)

    def inorderTraversal(self, root):
        result = []
        if root == None:
            return result
        self.helper(root, result)
        return result
    '''

    # Sol2: D & C
    '''
    def inorderTraversal(self, root):
        result = []
        if root == None:
            return result
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return left + [root.val] + right
    '''

    # Sol3: Iterative
    def inorderTraversal(self, root):
        result = []
        cur = root
        stack = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack[-1]
            result.append(cur.val)
            cur = cur.right
        return result




