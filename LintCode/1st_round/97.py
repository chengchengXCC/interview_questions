#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0
        lH = self.maxDepth(root.left)
        rH = self.maxDepth(root.right)
        return max(lH, rH) + 1

if __name__ == '__main__':
    s = Solution()
    #pdb.set_trace()
    print s.permuteUnique([1,2,2])









