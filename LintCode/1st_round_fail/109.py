#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
	# method1: DFS
	'''
	def helper(self, triangle, i, j, sum, result):
		if i == len(triangle) - 1:
			sum += triangle[i][j]
			if sum < result[0]:
				result[0] = sum
			return
		self.helper(triangle, i + 1, j, sum + triangle[i][j], result)
		self.helper(triangle, i + 1, j + 1, sum + triangle[i][j], result)


	def minimumTotal(self, triangle):
		result = []
		result.append(sys.maxint)
		if triangle == None or len(triangle) == 0:
			return result[0]
		self.helper(triangle, 0, 0, 0, result)
		return result[0]
	'''

	# method2: D & C
	'''
	def helper(self, triangle, i, j):
		if i == len(triangle) - 1:
			return triangle[i][j]
		left = self.helper(triangle, i + 1, j)
		right = self.helper(triangle, i + 1, j + 1)
		return max(left, right) + triangle[i][j]

	def minimumTotal(self, triangle):
		if triangle == None or len(triangle) == 0:
			return 0
		return self.helper(triangle, 0, 0)
	'''

	# method3: DP (bottom up)
	'''
	def minimumTotal(self, triangle):
		# initialization
		n = len(triangle)
		result = []
		for i in range(0, n):
			result.append([])
			for j in range(0, n):
				result[i].append(0)
	 	# construct result matrix (bottom up)
		i = len(triangle) - 1
		while i >= 0:
			for j in range(0, i + 1):
				if i == len(triangle) - 1:
					result[i][j] = triangle[i][j]
				else:
					result[i][j] = triangle[i][j] + min(result[i + 1][j], result[i + 1][j + 1])
			i -= 1
		return result[0][0]
	'''

	# method4: DP with memorization
	def helper(self, triangle, result, i, j):
		if i == len(triangle) - 1:
			result[i][j] = triangle[i][j]
			return result[i][j]
		if result[i][j] != sys.maxint:
			return result[i][j]
		result[i][j] = triangle[i][j] + min(self.helper(triangle, result, i + 1, j), self.helper(triangle, result, i + 1, j + 1))
		return result[i][j]
		
	def minimumTotal(self, triangle):
		n = len(triangle)
		result = []
		for i in range(0, n):
			result.append([])
			for j in range(0, n):
				result[i].append(sys.maxint)
		return self.helper(triangle, result, 0, 0)









