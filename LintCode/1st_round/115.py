#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
		matrix = []
		numOfRow = len(obstacleGrid)
		numOfCol = len(obstacleGrid[0])
		# initilization
		for i in range(0, numOfRow):
			matrix.append([])
			for j in range(0, numOfCol):
				matrix[i].append(-1)
		# initilize first column
		for i in range(0, numOfRow):
			if obstacleGrid[i][0] == 1:
				matrix[i][0] = 0
			elif i > 0 and matrix[i - 1][0] == 0:
				matrix[i][0] = 0
			else:
				matrix[i][0] = 1
		# initilize first row
		for j in range(0, numOfCol):
			if obstacleGrid[0][j] == 1:
				matrix[0][j] = 0
			elif j > 0 and matrix[0][j - 1] == 0:
				matrix[0][j] = 0
			else:
				matrix[0][j] = 1

		# construct rest of matrix
		for i in range(1, numOfRow):
			for j in range(1, numOfCol):
				if obstacleGrid[i][j] == 1:
					matrix[i][j] = 0
				else:
					matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
		return matrix[numOfRow - 1][numOfCol - 1]