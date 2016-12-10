#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
    def getDiff(self, a, b):
        if a >= b:
            return a - b
        else:
            return b - a

    def closestNumber(self, nums, x):
        if nums == None or len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == x:
                return mid
            elif nums[mid] > x:
                end = mid
            else:
                start = mid
        if self.getDiff(nums[start], x) <= self.getDiff(nums[end], x):
            return start
        else:
            return end
        
if __name__ == '__main__':
    s = Solution()
    #pdb.set_trace()
    print s.permuteUnique([1,2,2])









