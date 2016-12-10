'''
Time complexity: O(N*LogN)
class Solution:
    def getMax(self, nums, i, j):
        index = -1
        max_v = -sys.maxint
        for k in range(i, j + 1):
            if nums[k] > max_v:
                index = k
                max_v = nums[k]
        return index

    def helper(self, nums, i, j):
        if i > j:
            return None
        if i == j:
            return TreeNode(nums[i])
        mid = self.getMax(nums, i, j)
        root = TreeNode(nums[mid])
        leftT = self.maxTree(nums, i, mid - 1)
        rightT = self.maxTree(nums, mid + 1, j)
        root.left = leftT
        root.right = rightT
        return root

    def maxTree(self, nums):
        if nums == None or len(nums) == 0:
            return None
        return self.helper(nums, 0, len(nums) - 1)
'''

# Time complexity: O(N*LogN)
# Space complexity: O(N^2)
class Solution:
    def helper(self, nums, i, j, matrix):
        if i > j:
            return None
        if i == j:
            return TreeNode(nums[i])
        mid = matrix[i][j]
        root = TreeNode(nums[mid])
        leftT = self.helper(nums, i, mid - 1, matrix)
        rightT = self.helper(nums, mid + 1, j, matrix)
        root.left = leftT
        root.right = rightT
        return root

    def maxTree(self, nums):
        if nums == None or len(nums) == 0:
            return None
        # Construct 2d DP matrix
        matrix = []
        for i in range(0, len(nums)):
            matrix.append([])
            for j in range(0, len(nums)):
                if i == j:
                    matrix[i].append(i)
                else:
                    matrix[i].append(0)
        for i in range(0, len(nums)):
            max_v = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] > max_v:
                    max_v = nums[j]
                    matrix[i][j] = j
                else:
                    matrix[i][j] = matrix[i][j - 1]
        return self.helper(nums, 0, len(nums) - 1, matrix)
        




        