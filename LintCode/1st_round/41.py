class Solution:	
    '''
    Given the array [−2,2,−3,4,−1,2,1,−5,3], the contiguous subarray 
    [4,−1,2,1] has the largest sum = 6.
    '''
    # Time: O(N)
    def maxSubArray(self, nums):
        max_sum = 0
        tmp_sum = 0
        for i in range(0, len(nums)):
            tmp_sum += nums[i]
            if tmp_sum < 0:
                tmp_sum = 0
            else:
                if tmp_sum > max_sum:
                    max_sum = tmp_sum
        return max_sum
        