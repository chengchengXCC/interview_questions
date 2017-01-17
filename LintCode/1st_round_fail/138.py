class Solution:	
    '''
    Given nums = [1, 2, 4, 8, 6, 3] return 8
    Given nums = [10, 9, 8, 7], return 10
    '''
    # Space: O(N)
    # Time: O(N) 
    def subarraySum(self, nums):
        dict = {}
        dict[0] = -1
        sum = 0
        result = []
        for i in range(0, len(nums)):
            sum += nums[i]
            if sum in dict:
                result.append(dict[sum] + 1)
                result.append(i)
                break
            else:
                dict[sum] = i
        return result
