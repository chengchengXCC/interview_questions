#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
    def searchMatrix(self, matrix, x):
        count = 0
        if matrix == None:
            return 0
        numOfRow = len(matrix)
        if numOfRow == 0:
            return 0
        numOfCol = len(matrix[0])
        i = numOfRow - 1
        j = 0
        while i >= 0 and j < numOfCol:
            if matrix[i][j] == x:
                count += 1
                i -= 1
            elif matrix[i][j] < x:
                j += 1
            else:
                i -= 1
        return count


if __name__ == '__main__':
    s = Solution()
    #pdb.set_trace()
    print s.permuteUnique([1,2,2])









