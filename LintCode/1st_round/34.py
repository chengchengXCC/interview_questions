class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """

    def dfs_search(self, cols, n, result):
        if len(cols) == n:
            result[0] = result[0] + 1
            return
        for i in range(0, len(matrix)):
            if not self.isValid(cols, i):
                continue
            cols.append(i)
            self.dfs_search(cols, n, result)
            cols.pop()

    def isValid(self, cols, col):
        row = len(cols)
        for i in range(0, cols):
            if cols[i] == col:
                return False
            if i + cols[i] == row + col or i - cols[i] ==  row - col:
                return False
        return True 

    def totalNQueens(self, n):
        result = [0]
        self.dfs_search([], n, result)
        return result
