#!/usr/bin/python

import requests
import pdb
import sys

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
	"""
    @param a, b, the root of binary trees.
    @return true if they are tweaked identical, or false.
    """
    def isTweakedIdentical(self, a, b):
    	if a == None and b == None:
    		return true
    	if a == None or b == None:
    		return false
    	if a.val == b.val:
    		return self.isTweakedIdentical(a.left, b.left) and self.isTweakedIdentical(a.right, b.right)\
    				or self.isTweakedIdentical(a.left, b.right) and self.isTweakedIdentical(a.right, b.left)
    	else:
    		return false