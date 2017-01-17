class Solution:
	"""
	@param nums: A list of integers
	@param k: An integer denote to find k non-overlapping subarrays
	@return: An integer denote the sum of max k non-overlapping subarrays

	Given [-1,4,-2,3,-2,3], k=2, return 8

	"""
	
	def maxSubArray(self, nums, k):
		localMax = []
		for i in range(0, len(nums) + 1):
			localMax.append([])
			for j in range(0, k + 1):
				localMax[i].append(0)

		globalMax = []
		for i in range(0, len(nums) + 1):
			globalMax.append([])
			for j in range(0, k + 1):
				globalMax[i].append(0)

		for j in range(1, k + 1):
			localMax[j - 1][j] = -sys.maxint
			for i in range(j, len(nums) + 1):
				localMax[i][j] = max(globalMax[i - 1][j - 1], localMax[i - 1][j]) + nums[i - 1]
				if i == j:
				    globalMax[i][j] = localMax[i][j]
				else:
				    globalMax[i][j] = max(globalMax[i - 1][j], localMax[i][j])
		return globalMax[len(nums)][k]




		