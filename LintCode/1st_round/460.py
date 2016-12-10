class Solution:
    def getDiff(self, a, b):
        if a >= b:
            return a - b
        else:
            return b - a

    def findClosest(self, nums, x):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == x:
                return mid
            elif nums[mid] > x:
                end = mid
            else:
                start = mid
        if self.getDiff(nums[start], x) <= self.getDiff(nums[end], x):
            return start
        else:
            return end

    def kClosestNumbers(self, nums, x, k):
        result = []
        if nums == None or len(nums) == 0 or k <= 0 or k > len(nums):
            return result
        i = self.findClosest(nums, x)
        result.append(nums[i])
        left = i - 1
        right = i + 1
        k -= 1
        while k > 0:
            if left >=0 and right < len(nums):
                if self.getDiff(nums[left], x) <= self.getDiff(nums[right], x):
                    result.append(nums[left])
                    left -= 1
                else:
                    result.append(nums[right])
                    right += 1
            elif left >= 0:
                result.append(nums[left])
                left -= 1
            elif right < len(nums):
                result.append(nums[right])
                right += 1
            k -= 1
        return result