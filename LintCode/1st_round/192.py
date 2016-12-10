#!/usr/bin/python

class Solution:
	def isChar(self, c):
		if c != '*' and c != '?':
			return True
		else:
			return False

	def isMatch(self, str1, str2):
		if str1 == None or str2 == None:
			if str1 == None and str2 == None:
				return True
			else:
				return False
		m = len(str2) + 1
		n = len(str1) + 1
		matrix = []
		for i in range(0, m):
			matrix.append([])
			for j in range(0, n):
				matri[i].append(False)
		matrix[0][0] = True
		# initialize the first row
		for j in range(1, n):
			if matrix[0][j - 1] and str1[j - 1] == '*':
				matrix[0][j] = True
		for i in range(1, m):
			if matrix[i - 1][0] and str2[i - 1] == '*':
				matrix[i][0] = True
		# construct matrix 
		for i in range(1, m):
			for j in range(1, n):
				if str2[i - 1] == '*' or str1[j - 1] == '*':
					matrix[i][j] = matrix[i - 1][j - 1] or matrix[i - 1][j] or matrix[i][j - 1]
					continue
				if self.isChar(str2[i - 1]) and self.isChar(str1[j - 1]):
					matrix[i][j] = matrix[i - 1][j - 1] and str2[i - 1] == str1[j - 1]
					continue
				if self.isChar(str2[i - 1]) and str1[j - 1] == '?':
					matrix[i][j] = matrix[i - 1][j - 1]
					continue
				if str2[i - 1] == '?' or str1[j - 1] == '?':
					matrix[i][j] = matrix[i - 1][j - 1]
					continue
		return matrix[m - 1][n - 1]




