#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
	def lastPosition(self, nums, x):
		if nums == None or len(nums) == 0:
			return -1
		start = 0
		end = len(nums) - 1
		while start + 1 < end:
			mid = start + (end - start) / 2
			if nums[mid] < x:
				start = mid
			elif nums[mid] > x:
				end = mid
			else:
				start = mid
		if nums[end] == x:
			return end
		elif nums[start] == x:
			return start
		else:
			return -1