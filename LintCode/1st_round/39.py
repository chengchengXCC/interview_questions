class Solution:	
    '''
    [4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]
    '''
    def reverse(self, nums, start, end):
        while start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start += 1
            end -= 1

    def recoverRotatedSortedArray(self, nums):
        if nums == None or len(nums) == 0:
            return
        n = len(nums)
        if nums[0] <= nums[n - 1]:
            return
        i = n - 1
        while i >= 1:
            if nums[i] >= nums[i - 1]:
                i -= 1
            else:
                break
        self.reverse(nums, 0, i - 1)
        self.reverse(nums, i, n - 1)
        self.reverse(nums, 0, n - 1)

                
                
                
                    