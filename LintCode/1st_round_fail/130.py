class Solution:	
    # Sol1: sift down(自上而下)
    # Time Complexity: 
    '''
    def siftdown(self, nums, i):
        while i < len(nums):
            smallest = nums[i]
            k = i
            if 2 * i + 1 < len(nums) and nums[2 * i + 1] < smallest:
                smallest = nums[2 * i + 1]
                k = 2 * i + 1
            if 2 * i + 2 < len(nums) and nums[2 * i + 2] < smallest:
                smallest = nums[2 * i + 2]
                k = 2 * i + 2
            if k == i:
                break
            # swap
            tmp = nums[i]
            nums[i] = nums[k]
            nums[k] = tmp
            i += 1

    def heapify(self, nums):
        i = len(nums) / 2
        while i >= 0:
            self.siftdown(nums, i)
            i += 1
    '''
    # Time complexity: N*log(N)
    def siftUp(self, nums, i):
        while i > 0:
            # right T
            parent = -1
            if i % 2 == 0:
                parent = (i - 2) / 2
            else:
                parent = (i - 1) / 2
            if nums[parent] > nums[i]:
                tmp = nums[parent]
                nums[parent] = nums[i]
                nums[i] = tmp
                i = parent
            else:
                break

    def heapify(self, nums):
        i = len(nums) - 1
        while i > 0:
            self.siftUp(nums, i)
            i -= 1

        