#!/usr/bin/python

import requests
import pdb
import sys

# Sol1
class Solution:
	def searchMatrix(self, matrix, x):
		if matrix == None or len(matrix) == 0:
			return False
		numOfRow = len(matrix)
		numOfCol = len(matrix[0])
		i = numOfRow - 1
		j = 0
		while i >= 0 and j < numOfCol:
			if matrix[i][j] ==  x:
				return True
			elif matrix[i][j] > x:
				i -= 1
			else:
				j += 1
		return False

# Sol2:
class Solution:
	def searchInRow(self, row, x):
		start = 0
		end = len(row) - 1
		while start + 1 < end:
			mid = start + (end - start) / 2
			if row[mid] == x:
				return True
			elif row[mid] < x:
				start = mid
			else:
				end = mid
		if row[start] == x or row[end] == x:
			return True
		else:
			return False

	def searchMatrix(self, matrix, x):
		if matrix == None or len(matrix) == 0:
			return False
		numOfRow = len(matrix)
		numOfCol = len(matrix[0])
		start = 0
		end = numOfRow - 1
		while start + 1 < end:
			mid = start + (end - start) / 2
			if matrix[mid][0] <= x:
				start = mid
			else:
				end = mid
		if matrix[end][0] <= x:
			return self.searchInRow(matrix[end], x)
		elif matrix[start][0] <= x:
			return self.searchInRow(matrix[start], x)
		else:
			return False


if __name__ == '__main__':
    s = Solution()
    print s.searchMatrix([[5]], 2)

