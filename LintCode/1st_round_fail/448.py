#!/usr/bin/python

import requests
import pdb
import sys

class Solution(object):
	def leftMost(self, root):
		tmp = root
		while tmp.left:
			tmp = tmp.left
		return tmp

    def inorderSuccessor(self, root, p):
    	parent = None
    	tmp = root
    	while tmp.val != p.val:
    		if tmp.val < p.val:
    			tmp = tmp.right
    		else:
    			parent = tmp
    			tmp = tmp.left
    	if tmp.right:
    		return self.leftMost(tmp.right)
    	else:
    		return parent
	
if __name__ == '__main__':
   









