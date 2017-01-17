#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
	def longestIncreasingSubsequence(self, nums):
		if nums == None or len(nums) == 0:
			return 0
		array = []
		for i in range(0, len(nums)):
			if i == 0:
				array.append(1)
			else:
				array.append(-1)
		for i in range(1, len(nums)):
			max_len = 1
			for j in range(0, i):
				if nums[j] < nums[i] and array[j] + 1 > max_len:
					max_len = array[j] + 1
			array[i] = max_len
		return array[len(nums) - 1]
