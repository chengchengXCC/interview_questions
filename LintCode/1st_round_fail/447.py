#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
    # Time complexity: O(logK)
    def searchBigSortedArray(self, reader, x):
        i = 1
        while reader.get(i - 1) < x:
            i = i * 2
        start = 0
        end = i - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if reader.get(mid) == x:
                end = mid
            elif reader.get(mid) < x:
                start = mid
            else:
                end = mid
        if reader.get(start) == x:
            return start
        elif reader.get(end) == x:
            return end
        else:
            return -1

if __name__ == '__main__':
    s = Solution()
    #pdb.set_trace()
    print s.subsets([1,2])









