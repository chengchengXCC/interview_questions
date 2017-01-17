class Solution:	
    '''
    Given A=[1,2,3,4,5,6] and B=[2,3,4,5], the median is 3.5
    Given A=[1,2,3] and B=[4,5], the median is 3
    '''
    def findMedian(self, A, A_start, B, B_start, k):
        if A_start >= len(A):
            return B[B_start + k - 1]

        if B_start >= len(B):
            return A[A_start + k - 1]

        if k == 1:
            return min(A[A_start], B[B_start])

        A_key = 0
        B_key = 0    

        if A_start + k/2 - 1 < len(A):
            A_key = A[A_start + k/2 - 1]
        else:
            A_key = sys.maxint
        if B_start + k/2 - 1 < len(B):
            B_key = B[B_start + k/2 - 1]
        else:
            B_key = sys.maxint

        if A_key < B_key:
            return self.findMedian(A, A_start + k/2, B, B_start, k - k/2)
        else:
            return self.findMedian(A, A_start, B, B_start + k/2, k - k/2)


    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 0:
            return (self.findMedian(A, 0, B, 0, l/2) + self.findMedian(A, 0, B, 0, l/2 + 1)) / 2
        else:
            return (self.findMedian(A, 0, B, 0, l/2 + 1)


        

                
                
                
                    