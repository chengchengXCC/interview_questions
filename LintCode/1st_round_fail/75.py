#!/usr/bin/python

import requests
import pdb
import sys

# A[P] > A[P-1] && A[P] > A[P+1]
# Time complexity: O(logN)
class Solution:
    def findPeak(self, nums):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid
        if nums[start] > nums[end]:
            return start
        else:
            return end
