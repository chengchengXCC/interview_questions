#!/usr/bin/python

class Solution:
    # Sol1: Use an extra dictionary to store information
   	# Time: O(N)
   	# Space: 2*O(N)
    '''
    def removeDuplicates(self, head):
    	tmp = head
    	dict = {}
    	while tmp:
    		if tmp.val in dict:
    			dict[tmp.val] += 1
    		else:
    			dict[tmp.val] = 1
    		tmp = tmp.next
    	dummy = ListNode(-1)
    	dummy.next = head
    	tmp = dummy
    	dict_tmp = {}
    	while tmp.next:
    		if tmp.next.val not in dict_tmp:
    			key = tmp.next.val
    			tmp = tmp.next
    			dict_tmp[key] = 1
    			dict[key] -= 1
    			continue
    		if dict[tmp.next.val] > 0:
    			key = tmp.next.val
    			tmp.next = tmp.next.next
    			dict[key] -= 1
    		else:
    			tmp = tmp.next
    	return dummy.next
    '''
    # Sol2: Use one dict{}即可
    def removeDuplicates(self, head):
    	dummy = ListNode(-1)
    	dict = {}
    	dummy.next = head
    	tmp = dummy
    	while tmp.next:
    		if tmp.next.val not in dict:
    			key = tmp.next.val
    			tmp = tmp.next
    			dict[key] = 1
    		else:
    			tmp.next = tmp.next.next
    	return dummy.next

