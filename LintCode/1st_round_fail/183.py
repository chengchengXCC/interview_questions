#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
	def helper(self, L, l):
		result = 0
		for i in range(0, len(L)):
			result += L[i] / l
		return result

	# Time complexity: log(L_max) * len(L)
	def woodCut(self, L, k):
		start = 1
		end = 0
		for l in L:
			if l > end:
				end = l
		while start + 1 < end:
			mid = start + (end - start) / 2
			if self.helper(L, mid) >= k:
				start = mid
			else:
				end = mid
		if self.helper(L, end) >= k:
			return end
		elif self.helper(L, start) >= k:
			return start
		else:
			return 0