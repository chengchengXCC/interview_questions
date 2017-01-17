#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
    def longestCommonSubsequence(self, A, B):
		if A == None or B == None or len(A) == 0 or len(B) == 0:
			return 0
		n = len(A)
		m  = len(B)
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
				matrix[i][j] = max(max(matrix[i - 1][j], matrix[i][j - 1]), matrix[i - 1][j - 1])
				if B[i] == A[j]:
					matrix[i][j] = max(matrix[i][j], matrix[i - 1][j - 1] + 1)
		return matrix[m - 1][n - 1]

 
