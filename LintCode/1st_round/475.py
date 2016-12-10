#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
    def maxPathSum2(self, root):
        if root == None:
            return 0
        left = self.maxPathSum2(root.left)
        right = self.maxPathSum2(root.right)
        return max(0, max(left, right)) + root.val

if __name__ == '__main__':
   









