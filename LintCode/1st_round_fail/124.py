class Solution:
    def longestConsecutive(self, nums):
        if nums == None or len(nums) == 0:
            return 0
        dict = {}
        for num in nums:
            dict[num] = 1
        max_len = -sys.maxint
        for num in nums:
            down = num
            while down in dict:
                del dict[down]
                down -= 1
            up = num + 1
            while up in dict:
                del dict[up]
                up += 1
            max_len = max(max_len, up - down - 1)
        return max_len

