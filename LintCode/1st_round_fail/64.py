class Solution:	
    '''
    A = [1, 2, 3, empty, empty], B = [4, 5]
    After merge, A will be filled as [1, 2, 3, 4, 5]
    '''
    # Time: O(m + n) 
    def mergeSortedArray(self, A, m, B, n):
        i = len(A) - 1
        i_A = m - 1
        i_B = n - 1
        while i_A >= 0 and i_B >= 0:
            if A[i_A] > B[i_B]:
                A[i] = A[i_A]
                i -= 1
                i_A -= 1
            else:
                A[i] = B[i_B]
                i -= 1
                i_B -= 1
        while i_B >= 0:
            A[i] = B[i_B]
            i -= 1
            i_B -= 1