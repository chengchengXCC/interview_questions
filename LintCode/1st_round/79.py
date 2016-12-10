#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
	def longestCommonSubstring(self, A, B):
		if A == None or B == None or len(A) == 0 or len(B) == 0:
			return 0
		m = len(B)
		n = len(A)
		matrix = []
		for i in range(0, m):
			matrix.append([])
			for j in range(0, n):
				matrix[i].append(0)
		for i in range(0, m):
			if B[i] == A[0]:
				matrix[i][0] = 1
		for j in range(0, n):
			if B[0] == A[j]:
				matrix[0][j] = 1
		for i in range(1, m):
			for j in range(1, n):
				if B[i] == A[j]:
					matrix[i][j] = matrix[i - 1][j - 1] + 1
		max_len = -sys.maxint
		for i in range(0, m):
			for j in range(0, n):
				if matrix[i][j] > max_len:
					max_len = matrix[i][j]
		return max_len