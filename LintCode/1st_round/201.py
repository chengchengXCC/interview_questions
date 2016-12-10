#!/usr/bin/python

import requests
import pdb
import sys


"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None
"""
class Solution: 
    # @param start, end: Denote an segment / interval
    # @return: The root of Segment Tree
    def build(self, start, end):
        # write your code here
        if start > end:
            return None
        if start == end:
            return SegmentTreeNode(start, end)
        root = SegmentTreeNode(start, end)
        lT = self.build(start, (start + end) / 2)
        rT = self.build((start + end) / 2 + 1, end)
        root.left = lT
        root.right = rT
        return root   


if __name__ == '__main__':
    s = Solution()
    #pdb.set_trace()
    print s.permuteUnique([1,2,2])









