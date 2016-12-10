#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
    def lowestCommonAncestor(self, root, A, B):
    	if root == None or root == A or root == B:
    		return root
    	left = self.lowestCommonAncestor(root.left, A, B)
    	right = self.lowestCommonAncestor(root.right, A, B)
    	if left and right:
    		return root
    	elif left:
    		return left
    	elif right:
    		return right
    	else:
    		return None

if __name__ == '__main__':
    s = Solution()
    #pdb.set_trace()
    print s.permuteUnique([1,2,2])









