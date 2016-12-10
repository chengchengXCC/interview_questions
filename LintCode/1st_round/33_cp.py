class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def getSolution(self, matrix):
        result = []
        n = len(matrix)
        for i in range(0, n):
            tmp_result = ""
            for j in range(0, n):
                if matrix[i][j] == 1:
                    tmp_result += "Q"
                else:
                    tmp_result += "."
            result.append(tmp_result)
        return result

    def copyMatrix(self, matrix):
        new_matrix = []
        n = len(matrix)
        for i in range(0, n):
            new_matrix.append([])
            for j in range(0, n):
                new_matrix[i].append(matrix[i][j])
        return new_matrix

    def restoreMatrix(self, matrix, i, j):
        n = len(matrix)
        # col
        for k in range(i + 1, n):
            matrix[k][j] = 0
        # diagol + + 
        k = 1
        while i + k < n and j + k < n:
            matrix[i + k][j + k] = 0
            k += 1
        # diagol + -
        k = 1
        while i + k < n and j - k >= 0:
            matrix[i + k][j - k] = 0
            k += 1

    def flagMatrix(self, matrix, i, j):
        n = len(matrix)
        # change all related 0 to -1
        # current row
        #for k in range(0, n):
        #    if k != j and matrix[i][k] == 0:
        #        matrix[i][k] = -1
        # current col
        for k in range(i + 1, n):
            #if matrix[k][j] == 0:
            matrix[k][j] = -1
        # diagol + + 
        k = 1
        while i + k < n and j + k < n:
            #if matrix[i + k][j + k] == 0:
            matrix[i + k][j + k] = -1
            k += 1
        # diagnol - -
        #k = -1
        #while i + k >=0 and j + k >= 0:
        #    if matrix[i + k][j + k] == 0:
        #        matrix[i + k][j + k] = -1
        #    k -= 1
        # diagnol - +
        #k = 1
        #while i - k >=0 and j + k < n:
        #    if matrix[i - k][j + k] == 0:
        #        matrix[i - k][j + k] = -1
        #    k += 1
        # diagnol + -
        k = 1
        while i + k < n and j - k >= 0:
            #if matrix[i + k][j - k] == 0:
            matrix[i + k][j - k] = -1
            k += 1

    def dfs_search(self, row, matrix, result):
        if row == len(matrix):
            result.append(self.getSolution(matrix))
            return
        for i in range(0, len(matrix)):
            # if current pos is not taken
            # new_matrix = self.copyMatrix(matrix)
            if matrix[row][i] == 0:
                matrix[row][i] = 1
                # flag or non-available pos related to current pos (0->-1)
                self.flagMatrix(matrix, row, i)
                self.dfs_search(row + 1, matrix, result)
                #matrix = new_matrix
                matrix[row][i] = 0
                self.restoreMatrix(matrix, row, i)

    def solveNQueens(self, n):
        result = []
        # initialize matrix
        matrix = []
        for i in range(0, n):
            matrix.append([])
            for j in range(0, n):
                matrix[i].append(0)
        # do search recursively
        self.dfs_search(0, matrix, result)
        return result