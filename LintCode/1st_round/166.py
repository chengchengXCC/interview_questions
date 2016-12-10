class Solution:
	'''
	Given a List  3->2->1->5->null and n = 2, return node  whose value is 1.
	'''
	# Time Complexity: O(n)
	def getLen(self, head):
		n = 0
		tmp = head
		while tmp:
			n += 1
			tmp = tmp.next
		return n

	def nthToLast(self, head, n):
		if n > self.getLen(head) or n < 0:
			return None
		fast = head
		for i in range(1, n):
			fast = fast.next
		slow = head
		while fast.next:
			slow = slow.next
			fast = fast.next
		return slow


		