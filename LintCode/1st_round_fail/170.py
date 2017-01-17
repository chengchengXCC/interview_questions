#!/usr/bin/python

class Solution:
	def getLen(self, head):
		n = 0
		tmp = head
		while tmp:
			n += 1
			tmp = tmp.next
		return n

	def getTail(self, head):
		tmp = head
		while tmp.next:
			tmp = tmp.next
		return tmp

	def rotateRight(self, head, k):
		n = self.getLen(head)
		if n == 0:
			return head
		k = k % n
		if k == 0:
			return head
		k = n - k
		tmp = head
		for i in range(1, k):
			tmp = tmp.next
		dummy_head = ListNode(-1)
		dummy_head.next = tmp.next
		tmp.next = None
		self.getTail(dummy_head).next = head
		return dummy_head.next



			