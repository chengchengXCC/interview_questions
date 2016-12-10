#!/usr/bin/python

import requests
import pdb
import sys

# search insert position in a sorted array
'''
1,3,5,6 5-->2
1,3,5,6 2-->1
1,3,5,6 7-->4
1,3,5,6 0-->0
In this question, we need to find the first element, which is larger or equal to target element.
'''
class Solution:
    # Time complexity: O(logN)
    def searchInsert(self, nums, x):
        if nums == None or len(nums) == 0:
            return 0
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] < x:
                start = mid
            else:
                end = mid
        if nums[start] >= x:
            return start
        elif nums[end] >= x:
            return end
        else:
            return len(nums)
        

if __name__ == '__main__':
    s = Solution()
    #pdb.set_trace()
    print s.subsets([1,2])









