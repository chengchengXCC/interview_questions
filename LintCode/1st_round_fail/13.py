#!/usr/bin/python

class Solution:
	def strStr(self, source, target):
		if source == None or target == None or len(source) < len(target):
			return -1
		if len(target) == 0:
			return 0
		for i in range(0, len(source) - len(target) + 1):
			for j in range(0, len(target)):
				if source[i + j] != target[j]:
					break
				if j == len(target) - 1:
					return i
		return -1

# Time Complexity: O(n^2)
# Space Complexity: O(1)