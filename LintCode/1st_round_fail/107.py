#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
	def getMaxLen(self, dict):
		maxLen = -sys.maxint
		for word in dict:
			if len(word) > maxLen:
				maxLen = len(word)
		return maxLen

	def wordBreak(self, s, dict):
		if s == None or len(s) == 0:
			return True
		array = []
		for i in range(0, len(s) + 1):
			if i == 0:
				array.append(True)
			else:
				array.append(False)
		maxLen = self.getMaxLen(dict)
		for i in range(0, len(s)):
		    j = i
		    while j >= 0 and j >= i + 1 - maxLen:
				if array[j] and s[j:i+1] in dict:
					array[i + 1] = True
					break
				j -= 1
		return array[len(s)]