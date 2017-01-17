#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
    # Find Minimum in Rotated Sorted Array (no duplicates)
    # Time complexity: O(logN)
    def findMin(self, nums):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[start] > nums[mid]:
                end = mid
            elif nums[mid] > nums[end]:
                start = mid
            else:
                break
        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]

if __name__ == '__main__':
    s = Solution()
    #pdb.set_trace()
    print s.subsets([1,2])









