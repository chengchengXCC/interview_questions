class Solution:	
    '''
    All elements < k are moved to the left
    All elements >= k are moved to the right
    Return the partitioning index, i.e the first index i nums[i] >= k.
    If nums = [3,2,2,1] and k=2, a valid answer is 1.
    '''
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    # Time complexity: O(N)
    def partitionArray(self, nums, k):
        if nums == None or len(nums) == 0:
            return 0
        start = 0
        end = len(nums) - 1
        while start < end:
            while start < end and nums[start] < k:
                start += 1
            while start < end and nums[end] >= k:
                end -= 1
            if start < end:
                self.swap(nums, start, end)
                start += 1
                end -= 1
        for i in range(0, len(nums)):
            if nums[i] >= k:
                return i
        return i + 1



        