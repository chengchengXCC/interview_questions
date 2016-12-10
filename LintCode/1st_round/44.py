class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    For [1, -1, -2, 1], return -3
    """
    def minSubArray(self, nums):
        min_sum = sys.maxint
        tmp_sum = 0
        for i in range(0, len(nums)):
            tmp_sum += nums[i]
            if tmp_sum < min_sum:
                min_sum = tmp_sum
            if tmp_sum > 0:
                tmp_sum = 0
        return min_sum

        