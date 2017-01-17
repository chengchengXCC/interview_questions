#!/usr/bin/python

class Solution:
	# Time Complexity: O(N)
	def detectCycle(self, head):
		if head == None or head.next == None:
			return None
		slow = head
		fast = head.next
		# When slow meets with fast, slow walks n steps, and fast walks 2n steps. 
		# And 2n - n = n is the length of circle
		while slow != fast:
			if fast == None or fast.next == None:
				return None
			fast = fast.next.next
			slow = slow.next
		# slow is ahead of head n steps
		# when they meet, they must meet at the beginning of the circle
		while head != slow.next:
			slow = slow.next
			head = head.next
		return head
