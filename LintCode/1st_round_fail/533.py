class Solution:	
    '''
    Given array nums = [-1, 2, 1, -4], and target = 4.
    The minimum difference is 1. (4 - (2 + 1) = 1).
    '''
    def getDiffAbs(self, a, b):
        if a > b:
            return a - b
        else:
            return b - a

    # Time: O(N*LogN)
    def twoSumCloset(self, nums, target):
        nums.sort()
        start = 0
        end = len(nums) - 1
        min_diff = sys.maxint
        while start < end:
            tmp_sum = nums[start] + nums[end]
            tmp_diff = self.getDiffAbs(tmp_sum, target)
            if tmp_diff < min_diff:
                min_diff = tmp_diff
            if tmp_sum > target:
                end -= 1
            else:
                start += 1
        return min_diff


    
                
                
                    