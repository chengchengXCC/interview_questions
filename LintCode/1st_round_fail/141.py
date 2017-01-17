#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
	# find last num, so that num*num<=x
	# Time complexity: O(logN)
	def sqrt(self, x):
		start = 1
		end = x
		while start + 1 < end:
			mid = start + (end - start) / 2
			if mid * mid == x:
				return mid
			elif mid * mid < x:
				start = mid
			else:
				end = mid
		if end * end <= x:
			return end
		else:
			return start  