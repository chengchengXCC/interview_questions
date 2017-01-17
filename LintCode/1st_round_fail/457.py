#!/usr/bin/python
import requests
import pdb
import sys



class Solution:
    def findPosition(self, nums, x):
    	if nums == None or len(nums) == 0:
    		return -1
    	start = 0
    	end = len(nums) - 1
    	while start + 1 < end:
    		mid = (start + end) / 2
    		if nums[mid] == x:
    			return mid
    		elif nums[mid] < x:
    			start = mid + 1
    		else:
    			end = mid - 1
    	if nums[start] == x:
    		return start
    	elif nums[end] == x:
    		return end
    	else:
    		return -1

if __name__ == '__main__':
    s = Solution()
    #pdb.set_trace()
    print s.permuteUnique([1,2,2])