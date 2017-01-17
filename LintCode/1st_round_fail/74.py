#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
	# SVNRepo.isBadVersion
	# Find the first bad version
    def findFirstBadVersion(self, n):
    	start = 1
    	end = n
    	while start + 1 < end:
    		mid = start + (end - start) / 2
    		if SVNRepo.isBadVersion(mid):
    			end = mid
    		else:
    			start = mid
    	if SVNRepo.isBadVersion(start):
    		return start
    	else:
    		return end