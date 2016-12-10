#!/usr/bin/python

class Solution:
	# sol1: DP
	'''
	def canJump(self, A):
		jumpArray = []
		for i in range(0, len(A)):
			jumpArray.append(False)
		jumpArray[0] = True
		for i in range(0, len(A) - 1):
			if jumpArray[i]:
				for j in range(1, A[i] + 1):
					if i + j >= len(A):
						break
					jumpArray[i + j] = True
		return jumpArray[len(A) - 1]
	'''

	# sol2: Greedy method
	def canJump(self, A):
		farthest = A[0]
		for i in range(1, len(A)):
			if i <= farthest and i + A[i] > farthest:
				farthest = i + A[i]
		return farthest >= len(A) - 1

