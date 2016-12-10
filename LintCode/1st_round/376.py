#!/usr/bin/python

import requests
import pdb
import sys

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def helper(result, root, target, curSum, item):
        if root == None:
            return
        curSum += root.val
        item.append(root.val)
        if curSum == target and root.left == None and root.right == None:
            result.append(item)
        self.helper(root.left, target, curSum, item[:])
        self.helper(root.right, target, curSum, item[:])

    def binaryTreePathSum(self, root, target):
        result = []
        self.helper(result, root, target, 0, [])
        return result