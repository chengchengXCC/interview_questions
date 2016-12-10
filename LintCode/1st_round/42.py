class Solution:
    def maxTwoSubArrays(self, nums):
    	if nums == None or len(nums) == 0:
    		return 0
    	left = [0 for i in range(len(nums))]
    	right = [0 for i in range(len(nums))]
    	tmp_sum = 0
    	max_sum = -sys.maxint
    	for i in range(0, len(nums)):
    		tmp_sum += nums[i]
    		max_sum = max(max_sum, tmp_sum)
    		tmp_sum = max(0, tmp_sum)
    		left[i] = max_sum
    	tmp_sum = 0
    	max_sum = -sys.maxint
    	for i in range(0, len(nums))[::-1]:
    		tmp_sum += nums[i]
    		max_sum = max(max_sum, tmp_sum)
    		tmp_sum = max(0, tmp_sum)
    		right[i] = max_sum
    	max_sum = -sys.maxint
    	for i in range(0, len(nums) - 1):
    		max_sum = max(max_sum, left[i] + right[i + 1])
    	return max_sum

		