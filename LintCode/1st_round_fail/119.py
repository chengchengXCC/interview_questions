class Solution:	
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        matrix = []
        if m == 0:
            return n
        if n == 0:
            return m
        for i in range(0, m + 1):
            matrix.append([])
            for j in range(0, n + 1):
                matrix.append(-1)
        for i in range(0, m + 1):
            matrix[i][0] = i
        for j in range(0, n):
            matrix[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i] == word2[j]:
                    matrix[i][j] = matrix[i - 1][j - 1]
                else:
                    matrix[i][j] = min(min(matrix[i - 1][j], matrix[i][j - 1]), matrix[i - 1][j - 1]) + 1
        return matrix[m][n]
        