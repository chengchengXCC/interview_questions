#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
	def getIsPalindrom(self, s):
		n = len(s)
		isPalinArray = []
		for i in range(0, n):
			isPalinArray.append([])
			for j in range(0, n):
				isPalinArray[i].append(False)
		for i in range(0, n):
			isPalinArray[i][i] = True
		for i in range(0, n - 1):
			if s[i] == s[i + 1]:
			isPalinArray[i][i + 1] = True
		l = 2
		while l < n:
			for i in range(0, n - l):
				if s[i] == s[i + l] and s[i + 1] == s[i + l - 1]:
					isPalinArray[i][i + l] = True
			l += 1
		return isPalinArray

	def minCut(self, s):
		if s == None or len(s) == 0:
			return 0		
		isPalinArray = self.getIsPalindrom(s)
		array = []
		for i in range(0, len(s) + 1):
			array.append(i - 1)
		for i in range(1, len(s) + 1):
			for j in range(0, i):
				if isPalinArray[j][i - 1]:
					array[i] = min(array[i], array[j] + 1)
		return array[len(s)]

