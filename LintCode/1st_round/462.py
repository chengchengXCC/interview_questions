#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
    def findFirst(self, nums, x):
        if nums == None or len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] >= x:
                end = mid
            else:
                start = mid
        if nums[start] == x:
            return start
        elif nums[end] == x:
            return end
        else:
            return -1

    def findLast(self, nums, x):
        if nums == None or len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] > x:
                end = mid
            else: 
                start = mid
        if nums[end] == x:
            return end
        elif nums[start] == x:
            return start
        else:
            return -1

    def totalOccurrence(self, nums, x):
        start = self.findFirst(nums, x)
        end = self.findLast(nums, x)
        if start == -1 or end == -1:
            return 0
        else:
            return end - start + 1


if __name__ == '__main__':
    s = Solution()
    #pdb.set_trace()
    print s.permuteUnique([1,2,2])









