class Solution:
    # @param {int} n an integer
    # @return {int} an integer
    def dropEggs(self, n):
        matrix = []
        for i in range(0, 3):
            matrix.append([])
            for j in range(0, n + 1):
                matrix[i] = 0
        for i in range(1, 3):
            for j in range(1, n + 1):
                if j == 1:
                    matrix[i][1] = 1
                elif i == 1:
                    matrix[1][j] = j
        for i in range(2, 3):
            for j in range(2, n + 1):
                res = sys.maxint
                for x in range(1, j + 1):
                    tmp = max(matrix[i - 1][x - 1], matrix[i][j - x])
                    if tmp < res:
                        res = tmp
        return matrix[2][n + 1]

        