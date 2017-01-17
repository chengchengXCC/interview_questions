class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two Subarrays
    """
    def diffAbs(self, a, b):
        if a > b:
            return a - b
        else:
            return b - a

    def maxDiffSubArrays(self, nums):
        l_max = [0 for i in range(len(nums))]
        r_min = [0 for i in range(len(nums))]
        l_min = [0 for i in range(len(nums))]
        r_max = [0 for i in range(len(nums))]

        # Construct l_max
        tmp_max = -sys.maxint
        sum = 0
        for i in range(0, len(nums)):
            sum += nums[i]
            if sum > tmp_max:
                tmp_max = sum
            if sum < 0:
                sum = 0
            l_max[i] = tmp_max

        # Construct r_min
        tmp_min = sys.maxint
        sum = 0
        for i in range(len(nums)-1, -1, -1):
            sum += nums[i]
            if sum < tmp_min:
                tmp_min = sum
            if sum > 0:
                sum = 0
            r_min[i] = tmp_min

        # Construct l_min
        tmp_min = sys.maxint
        sum = 0
        for i in range(0, len(nums)):
            sum += nums[i]
            if sum < tmp_min:
                tmp_min = sum
            if sum > 0:
                sum = 0
            l_min[i] = tmp_min

        # Construct r_max
        tmp_max = -sys.maxint
        sum = 0
        for i in range(len(nums)-1, -1, -1):
            sum += nums[i]
            if sum > tmp_max:
                tmp_max = sum
            if sum < 0:
                sum = 0
            r_max[i] = tmp_max

        result = 0
        for i in range(0, len(nums) - 1):
            result = max(result, self.diffAbs(l_max[i], r_min[i + 1]))
            result = max(result, self.diffAbs(l_min[i], r_max[i + 1]))
        return result









        