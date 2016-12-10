class Solution:	
    #S = "rabbbit", T = "rabbit", return 3.
    # sol1: space cost: O(N^2)
    '''
    def numDistinct(self, S, T):
        m = len(S)
        n = len(T)
        matrix = []
        for i in range(0, m + 1):
            matrix.append([])
            for j in range(0, n + 1):
                matrix[i].append(-1)
        for i in range(0, m + 1):
            matrix[i][0] = 1
        for j in range(1, n + 1):
            matrix[0][j] = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if S[i - 1] == T[j - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j]
                else:
                    matrix[i][j] = matrix[i - 1][j]
        return matrix[m][n]
    '''

    # Sol2: space cost: O(N)
    def numDistinct(self, S, T):
        array = []
        for i in range(0, 2):
            array.append([])
            for j in range(0, len(T) + 1):
                array[i].append(-1)
        for j in range(0, len(T) + 1):
            if j == 0:
                array[0][j] = 1
            else:
                array[0][j] = 0
        for i in range(0, len(S)):
            if i % 2 == 0:
                for j in range(0, len(T) + 1):
                    if j == 0:
                        array[1][j] = 1
                    else:
                        if S[i] == T[j - 1]:
                            array[1][j] = array[0][j] + array[0][j - 1]
                        else:
                            array[1][j] = array[0][j]
            else:
                for j in range(0, len(T) + 1):
                    if j == 0:
                        array[0][j] = 1
                    else:
                        if S[i] == T[j - 1]:
                            array[0][j] = array[1][j] + array[1][j - 1]
                        else:
                            array[0][j] = array[1][j]
        if len(S) % 2 == 0:
            return array[0][len(T)]
        else:
            return array[1][len(T)]



