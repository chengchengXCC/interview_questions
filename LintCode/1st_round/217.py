#!/usr/bin/python

class Solution:
	# Time Complexity: O(N)
    def removeElements(self, head, val):
    	dummy = ListNode(-1)
    	dummy.next = head
    	tmp = dummy
    	while tmp.next:
    		if tmp.next.val == val:
    			tmp.next = tmp.next.next
    		else:
    			tmp = tmp.next
    	return dummy.next



		