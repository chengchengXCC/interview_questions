# Sol1: iterative
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        nums.sort()
        result = [[]]
        tmp_n = 0
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                n = len(result)
                for j in range(n-tmp_n, n):
            else:
                n = len(result)
                for j in range(0, n):
                    result.append(result[j] + [nums[i]])
                tmp_n = len(result) - n
        return result

# Sol2: 
class Solution:
    def helper(self, pos, item, result, nums, taken):
        if pos == len(nums):
            result.append(item[:])
            return
        if pos == 0 or nums[pos] != nums[pos - 1] or nums[pos] == nums[pos - 1] and taken:
            self.helper(pos + 1, item, result, nums, false)
            self.helper(pos + 1, item + [nums[pos]], result, nums, true)
        else:
            self.helper(pos + 1, item, result, nums, false)

    def subsetsWithDup(self, nums):
        nums.sort()
        result = [[]]
        self.helper(0, [], result, nums, False)
        return result



# Sol3: recursive 2

class Solution:
    def helper(self, pos, item, nums, result):
        result.append(item[:])
        for i in range(pos, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            item.append(nums[i])
            self.helper(i + 1, item, nums, result)
            item.pop()
                
    def subsetsWithDup(self, nums):
        nums.sort()
        result = []
        self.helper(0, [], nums, result)
        return result









