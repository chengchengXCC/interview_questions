class Solution:	
    '''
    Given [5, 7, 7, 8, 8, 10] and target value 8,
    return [3, 4].
    '''
    def findFirst(self, nums, x):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] > x:
                end = mid
            elif nums[mid] < x:
                start = mid
            else:
                end = mid
        if nums[start] == x:
            return start
        elif nums[end] == x:
            return end
        else:
            return -1    

    def findLast(self, nums, x):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] > x:
                end = mid
            elif nums[mid] < x:
                start = mid
            else:
                start = mid
        if nums[end] == x:
            return end
        elif nums[start] == x:
            return start
        else:
            return -1   

    def searchRange(self, nums, x):    
        if nums == None or len(nums) == 0:
            return [-1, -1]
        return [self.findFirst(nums, x), self.findLast(nums, x)]
                    
                
                
                
                    