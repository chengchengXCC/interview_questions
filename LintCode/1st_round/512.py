#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
	def numDecodings(self, s):
		if s == None or len(s) == 0:
			return 0
		for i in range(0, len(s)):
			if i == 0:
				if s[i] == '0':
					return 0
			else:
				if s[i] == '0' and s[i - 1] == '0':
					return 0
		array = []
		for i in range(0, len(s) + 1):
			array.append(0)
		for i in range(0, len(s) + 1):
			if i == 1 or i == 0:
				array[i] = 1
			else:
				if s[i - 1] == '0':
					if int(s[i - 2]) > 2:
						return 0
					else:
						array[i] = array[i - 2]
				else:
					num = int(s[i-2:i])
					if num >= 1 and num <= 26:
						array[i] = array[i - 1] + array[i - 2]
					else:
						array[i] = array[i - 1]
		return array[len(s)]


