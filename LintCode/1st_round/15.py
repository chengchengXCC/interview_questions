#!/usr/bin/python

import requests
import pdb
import sys


# Sol1: Recursive

class Solution:
    def helper(self, item, is_visited, nums, result):
        if len(item) == len(nums):
            result.append(item)
            return
        for i in range(0, len(nums)):
            if is_visited[i] == False:
                item.append(nums[i])
                is_visited[i] = True
                self.helper(item, is_visited, nums, result)
                item.pop()
                is_visited[i] = False
    def permute(self, nums):
        nums.sort()
        result = []
        is_visited = []
        for i in range(0, len(nums)):
            is_visited.append(False)
        self.helper([], is_visited, nums, result)
        return result

# Sol2: Iterative

class Solution:
    def permute(self, nums):
        nums.sort()
        result = [[]]
        while len(result[0]) < len(nums):
            new_result = []
            for item in result:
                for num in nums:
                    if num not in item:
                        new_result.append(item + [num])
            result = new_result
        return result

        




