#!/usr/bin/python

class Solution:
	# sol1: DP
	'''
	def jump(self, A):
		if A == None or len(A) == 0:
			return False
		canJumpArray = []
		for i in range(0, len(A)):
			if i == 0:
				canJumpArray.append(0)
			else:
				canJumpArray.append(-1)
		for i in range(1, len(A)):
			minStep = sys.maxint
			for j in range(0, i):
				if canJumpArray[j] != -1 and j + A[j] >= i and canJumpArray[j] + 1 < minStep:
					minStep = canJumpArray[j] + 1
			canJumpArray[i] = minStep
		return canJumpArray[len(A) - 1]
	'''

	# sol2: greedy
	def jump(self, A):
		start = 0
		end = 0
		jumps = 0
		while end < len(A) - 1:
			jumps += 1
			farthest = end
			for i in range(start, end + 1):
				if i + A[i] > farthest:
					farthest = i + A[i]
			start = end + 1
			end = farthest
		return jumps


