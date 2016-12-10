#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
	def minPathSum(self, grid):
		matrix = []
		numOfRow = len(grid)
		numOfCol = len(grid[0])
		# initialization
		for i in range(0, numOfRow):
			matrix.append([])
			for j in range(0, numOfCol):		
				matrix[i].append(0)
		# initialize first row
		tmpSum = 0
		for j in range(0, numOfCol):
			tmpSum += grid[0][j]
			matrix[0][j] = tmpSum
		# initilize first column
		tmpSum = 0
		for i in range(0, numOfRow):
			tmpSum += grid[i][0]
			matrix[i][0] = tmpSum
		for i in range(1, numOfRow):
			for j in range(1, numOfCol):
				matrix[i][j] = grid[i][j] + min(matrix[i - 1][j], matrix[i][j - 1])
		return matrix[numOfRow - 1][numOfCol - 1]