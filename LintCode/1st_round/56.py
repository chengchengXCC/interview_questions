
class Node:
    def __init__(self, _value, _pos):
        self.value = _value
        self.pos = _pos
    def __cmp__(self, other):
        if self.value == other.value:
            return self.pos - other.pos
        return self.value - other.value 

class Solution:
    '''
    The function twoSum should return indices of the two numbers such that 
    they add up to the target, where index1 must be less than index2. 
    Please note that your returned answers (both index1 and index2) are NOT zero-based.
    Ex:
        numbers=[2, 7, 11, 15], target=9
        return [1, 2]
    '''
    # Sol 1
    # O(n) Space, O(nlogn) Time
    '''
    def twoSum(self, nums, target):
        set = []
        new_set = []
        result = []
        for i in range(0, len(nums)):
            set.append(Node(nums[i], i + 1))
        # N*log(N)
        new_set = sorted(set)
        start = 0
        end = len(new_set) - 1
        while start < end:
            tmp_target = new_set[start].value + new_set[end].value
            if tmp_target == target:
                if new_set[start].pos < new_set[end].pos:
                    result.append(new_set[start].pos)
                    result.append(new_set[end].pos)
                else:
                    result.append(new_set[end].pos)
                    result.append(new_set[start].pos)
                break
            elif tmp_target < target:
                start += 1
            else:
                end -= 1
        return result
    '''

    # Sol 2
    # O(n) Space, O(n) Time
    def twoSum(self, nums, target):
        dict = {}
        for i in range(0, len(nums):
            if nums[i] not in dict:
                set = []
                set.append(i)
                dict[nums[i]] = set
            else:
                dict[nums[i]].append(i)
        result = []
        for i in range(0, len(nums)):
            x = target - nums[i]
            if x == nums[i]:
                if len(dict[x]) > 1:
                    result.append(dict[x][0])
                    result.append(dict[x][1])
                    break
            else:
                if x in dict:
                    result.append(i)
                    result.append(dict[x][0])
                    break
        return result



      