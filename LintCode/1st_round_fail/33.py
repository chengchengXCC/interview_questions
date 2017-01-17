class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def getSolution(self, cols, n):
        result = []
        for i in range(0, n):
            tmp_result = ""
            for j in range(0, n):
                if j == cols[i]:
                    tmp_result += "Q"
                else:
                    tmp_result += "."
            result.append(tmp_result)
        return result

    def dfs_search(self, cols, n, result):
        if len(cols) == n:
            result.append(self.getSolution(cols, n))
            return
        for i in range(0, n):
            if not self.isValid(cols, i):
                continue
            cols.append(i)
            self.dfs_search(cols, n, result)
            cols.pop()

    def isValid(self, cols, col):
        row = len(cols)
        for i in range(0, len(cols)):
            if cols[i] == col:
                return False
            if i + cols[i] == row + col or i - cols[i] ==  row - col:
                return False
        return True 

    def solveNQueens(self, n):
        result = []
        self.dfs_search([], n, result)
        return result
