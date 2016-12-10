#!/usr/bin/python

class Solution:
	# Time Complexity: O(N)
    def middleNode(self, head):
		if head == None or head.next == None:
			return head
		slow = head
		fast = head.next
		while fast:
			if fast.next:
				fast = fast.next.next
				slow = slow.next
			else:
			    break
		return slow