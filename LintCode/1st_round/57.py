class Solution:
    def threeSum(self, nums):
        result = []
        if nums == None or len(nums) == 0:
            return result
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            start = i + 1
            end = len(nums) - 1
            while start < end:
                tmp = nums[i] + nums[start] + nums[end]
                if tmp == 0:
                    result.append([nums[i], nums[start], nums[end]])
                    tmp = nums[start]
                    start += 1
                    while start < end and nums[start] == tmp:
                        start += 1
                    tmp = nums[end]
                    end -= 1
                    while start < end and nums[end] == tmp:
                        end -= 1
                elif tmp > 0:
                    end -= 1
                else:
                    start += 1
            tmp = nums[i]
            i += 1
            while i < len(nums) - 2 and nums[i] == tmp:
                i += 1
        return result


    