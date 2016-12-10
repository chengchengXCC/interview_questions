#!/usr/bin/python

import requests
import pdb
import sys


# Sol1: Iterative
# Time: O(2^N)
class Solution:
	def subsets(self, nums):
		nums.sort()
		result = [[]]
		for num in nums:
			n = len(result)
			for i in range(0, n):
				if num not in result[i]:
					result.append(result[i] + [num])
		return result


# Sol2: Recursive 1
# Time: T(2^N)
class Solution:
	def helper(self, pos, item, result, nums):
		if pos == len(nums):
			result.append(item[:])
			return
		self.helper(pos + 1, item + [nums[pos]], result, nums)
		self.helper(pos + 1, item, result, nums)

	def subsets(self, nums):
		nums.sort()
		result = [[]]
		self.helper(0, [], result, nums)
		return result


# Recursive 2
# Time: O(2^N)
class Solution:
		def helper(self, pos, item, nums, result):
				result.append(item[:])
				for i in range(pos, len(nums)):
						item.append(nums[i])
						self.helper(i + 1, item, nums, result)
						item.pop()
				
		def subsets(self, nums):
				nums.sort()
				result = []
				self.helper(0, [], nums, result)
				return result



