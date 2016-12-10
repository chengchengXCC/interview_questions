class Solution:
    """
        @param nums: a list of integers
        @return: A integer denote the sum of minimum subarray
        For [1, -1, -2, 1], return -3
    """
    def maxProduct(self, nums):
        max_p = [0 for i in range(len(nums))]
        min_p = [0 for i in range(len(nums))]
        result = nums[0]
        max_p = min_p = nums[0]
        for i in range(1, len(nums)):
            max_p[i] = min_p[i] = nums[i]
            if nums[i] > 0:
                max_p[i] = max(max_p[i], max_p[i] * max_p[i-1])
                min_p[i] = max(min_p[i], min_p[i] * min_p[i-1])
            elif nums[i] < 0:
                max_p[i] = max(max_p[i], max_p[i] * min_p[i-1])
                min_p[i] = max(min_p[i], min_p[i] * max_p[i-1])
            result = max(result, max_p[i])
        return result
        
        