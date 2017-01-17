class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
    	i_A = 0
    	i_B = 0
    	new_array = []
    	while i_A < len(A) and i_B < len(B):
    		if A[i_A] < B[i_B]:
    			new_array.append(A[i_A])
    			i_A += 1
    		else:
    			new_array.append(B[i_B])
    			i_B += 1
    	while i_A < len(A):
    		new_array.append(A[i_A])
    		i_A += 1
    	while i_B < len(B):
    		new_array.append(B[i_B])
    		i_B += 1
    	return new_array