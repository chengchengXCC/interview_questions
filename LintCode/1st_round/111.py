#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
	def climbStairs(self, n):
		if n == 0:
			return 1
		array = []
		for i in range(0, n):
			if i == 0:
				array.append(1)
			elif i == 1:
				array.append(2)
			else:
				array.append(array[i - 2] + array[i - 1])
		return array[n - 1]
