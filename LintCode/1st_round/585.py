class Solution:	
    '''
    Given nums = [1, 2, 4, 8, 6, 3] return 8
    Given nums = [10, 9, 8, 7], return 10
    '''
    # Log(N)
    def mountainSequence(self, nums):
        if len(nums) == 1:
            return nums[0]
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return nums[mid]
            if nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid
        if nums[start] > nums[end]:
            return nums[start]
        else:
            return nums[end]
                
                    