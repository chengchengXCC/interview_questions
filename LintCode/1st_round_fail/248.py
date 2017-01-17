#!/usr/bin/python

import requests
import pdb
import sys

# Time complexity: 

# Sol1: sort array & do b-search
class Solution:

    def bSearch(self, nums, x):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] >= x:
                end = mid
            else:
                start = mid
        if nums[start] >= x:
            return start
        else:
            return end

    def countOfSmallerNumber(self, nums, queries):
        result = []
        nums.sort()
        for x in queries:
            if len(nums) == 0:
                result.append(0)
            else:
                result.append(self.bSearch(nums, x))
        return result

