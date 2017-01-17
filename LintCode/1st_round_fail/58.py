class Solution:
    # Time: O(N^3)
    def fourSum(self, nums, target):
        result = []
        if nums == None or len(nums) == 0:
            return result
        nums.sort()
        i = 0
        while i < len(nums) - 3:
            j = i + 1
            while j < len(nums) - 2:
                start = j + 1
                end = len(nums) - 1
                while start < end:
                    tmp = nums[i] + nums[j] + nums[start] + nums[end]
                    if tmp == target:
                        result.append([nums[i], nums[j], nums[start], nums[end]])
                        tmp = nums[start]
                        start += 1
                        while start < end and nums[start] == tmp:
                            start += 1
                        tmp = nums[end]
                        end -= 1
                        while start < end and nums[end] == tmp:
                            end -= 1
                    elif tmp > target:
                        end -= 1
                    else:
                        start += 1
                tmp = nums[j]
                j += 1
                while j < len(nums) - 2 and nums[j] == tmp:
                    j += 1
            tmp = nums[i]
            i += 1
            while i < len(nums) - 3 and nums[i] == tmp:
                i += 1
        return result

        