class Solution:	
    '''
    Given [1, 0, 1, 2], sort it in-place to [0, 1, 1, 2].
    '''
    def swap(self, nums, i, j):
    	tmp = nums[i]
    	nums[i] = nums[j]
    	nums[j] = tmp

    def sortColors(self, nums):
    	i = 0
    	l = 0
    	r = len(nums) - 1
    	while i <= r:
    		if nums[i] == 1:
    			i += 1
    		elif nums[i] == 0:
    			self.swap(nums, i, l)
    			i += 1
    			l += 1
    		else:
    			self.swap(nums, i, r)
    			r -= 1

        
        

                
                
                
                    