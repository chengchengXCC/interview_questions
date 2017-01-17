class Solution:	
    '''
    Given nums = [1, 2, 4, 8, 6, 3] return 8
    Given nums = [10, 9, 8, 7], return 10
    '''
    # Sol1: sort & sort
    # N log N
    '''
    def intersection(self, nums1, nums2):
        result = []
        nums1.sort()
        nums2.sort()
        i1 = 0
        i2 = 0
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] == nums2[i2]:
                result.append(nums1[i1])
                tmp = nums1[i1]
                while i1 < len(nums1) and nums1[i1] == tmp:
                    i1 += 1
                while i2 < len(nums2) and nums2[i2] == tmp:
                    i2 += 1
            elif nums1[i1] < nums2[i2]:
                tmp = nums1[i1]
                while i1 < len(nums1) and nums1[i1] == tmp:
                    i1 += 1
            else:
                tmp = nums2[i2]
                while i2 < len(nums2) and nums2[i2] == tmp:
                    i2 += 1
        return result
    '''
    # Sol2: HashMap
    # Time: O(N)
    # Space: O(N)
    '''
    def intersection(self, nums1, nums2):
        dict = {}
        result = []
        for num in nums1:
            if num not in dict:
                dict[num] = 1
        for num in nums2:
            if num in dict:
                if dict[num] == 1:
                    result.append(num)
                    dict[num] = 0
        return result
    '''
    # Sol3: sort and bsearch
    def bsearch(self, nums, x):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] == x:
                return True
            elif nums[mid] < x:
                start = mid
            else:
                end = mid
        if nums[start] == x or nums[end] == x:
            return True
        else:
            return False

    def intersection(self, nums1, nums2):
        nums1.sort()
        result = []
        if len(nums1) == 0 or len(nums2) == 0:
            return result
        i = 0
        while i < len(nums2):
            tmp = nums2[i]
            if tmp in result:
                continue
            if self.bsearch(nums1, tmp):
                result.append(tmp)
            while i < len(nums2) and nums2[i] == tmp:
                i += 1
        return result






        