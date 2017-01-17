import sys 

class Node:
    def __init__(self, _value, _pos):
        self.value = _value
        self.pos = _pos
    def __cmp__(self, other):
        if self.value == other.value:
            # if value is same
            return self.pos - other.pos
        return self.value - other.value 
        
class Solution:
    def diffAbs(self, a, b):
        if a > b:
            return a - b
        else:
            return b - a

    def subarraySumClosest(self, nums):
        res = []
        result = []
        res.append(Node(0, -1))
        sum = 0
        for i in range(0, len(nums)):
            sum += nums[i]
            res.append(Node(sum, i))
        s = []
        s = sorted(res)
        result.append(-1)
        result.append(-1)
        min_diff = sys.maxint
        for i in range(1, len(s)):
            tmp_diff = self.diffAbs(s[i - 1].value, s[i].value)
            if tmp_diff < min_diff:
                min_diff = tmp_diff
                if s[i - 1].pos < s[i].pos:
                    result[0] = s[i - 1].pos + 1
                    result[1] = s[i].pos
                else:
                    result[0] = s[i].pos + 1
                    #print s[i-1].value, s[i-1].pos
                    result[1] = s[i - 1].pos

        return result

if __name__ == '__main__':
    s = Solution()
    print s.subarraySumClosest([-3, 1, 1, -3, 5])
                
                
                    