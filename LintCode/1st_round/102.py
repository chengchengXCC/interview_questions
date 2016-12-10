#!/usr/bin/python

class Solution:
	# sol: fast node & slow node
	def hasCycle(self, head):
		if head == None or head.next == None:
			return False
		slow = head
		fast = head.next
		while slow != fast:
			if fast == None or fast.next == None:
				return False
			fast = fast.next.next
			slow = slow.next
		return True


		