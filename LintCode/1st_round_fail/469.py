#!/usr/bin/python

import requests
import pdb
import sys
import Queue

class Solution:
	def isIdentical(self, a, b):
		if a == None and b == None:
			return True
		if a == None or b == None:
			return False
		if a.val == b.val:
			return self.isIdentical(a.left, b.left) and self.isIdentical(a.right, b.right)
		else:
			return False

if __name__ == '__main__':
   









