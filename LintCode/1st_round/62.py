#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
	def search(self, nums, x):
		if nums == None or len(nums) == 0:
			return -1
		start = 0
		end = len(nums) - 1
		while start + 1 < end:
			mid = start + (end - start) / 2
			if nums[start] < nums[mid]:
				if nums[start] <= x and x <= nums[mid]:
					end = mid
				else:
					start = mid
			else:
				if nums[mid] <= x and x <= nums[end]:
					start = mid
				else:
					end = mid
		if nums[start] == x:
			return start
		elif nums[end] == x:
			return end
		else:
			return -1


		