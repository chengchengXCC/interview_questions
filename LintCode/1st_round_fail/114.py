#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
    def uniquePaths(self, m, n):
		matrix = []
		for i in range(0, m):
			matrix.append([])
			for j in range(0, n):
				if i == 0 or j == 0:
					matrix[i].append(1)
				else:
					matrix[i].append(0)
		for i in range(1, m):
			for j in range(1, n):
				matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
		return matrix[m - 1][n - 1]