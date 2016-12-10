class Solution:	
    def isInterleave(self, s1, s2, s):
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s)
        if n1 + n2 != n3:
            return False
        matrix = []
        for i in range(0, n1 + 1):
            matrix.append([])
            for j in range(0, n2 + 1):
                matrix[i].append(False)
        for i in range(0, n1 + 1):
            if s1[0:i] == s[0:i]:
                matrix[i][0] = True
        for j in range(0, n2 + 1):
            if s2[0:j] == s[0:j]:
                matrix[0][j] = True
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s[i + j - 1] and matrix[i - 1][j]:
                    matrix[i][j] = True
                elif  s2[j - 1] == s[i + j - 1] and matrix[i][j - 1]:
                    matrix[i][j] = True
        return matrix[n1][n2]

