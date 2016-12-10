#!/usr/bin/python

import requests
import pdb
import sys


# Sol1: Recursive

class Solution:
    def helper(self, item, is_visited, nums, result):
        if len(item) == len(nums):
            result.append(item[:])
        for i in range(0, len(nums)):
            if not is_visited[i]:
                if i == 0 or nums[i] != nums[i - 1] or is_visited[i - 1]:
                    is_visited[i] = True
                    item.append(nums[i])
                    self.helper(item, is_visited, nums, result)
                    is_visited[i] = False
                    item.pop()
        
    def permuteUnique(self, nums):
        nums.sort()
        result = []
        is_visited = []
        for i in range(0, len(nums)):
            is_visited.append(False)
        self.helper([], is_visited, nums, result)
        return result






