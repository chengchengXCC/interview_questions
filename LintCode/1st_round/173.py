#!/usr/bin/python

class Solution:
	# Time Complexity: O(n^2)
	def getLen(self, head):
		n = 0
		tmp = head
		while tmp:
			n += 1
			tmp = tmp.next
		return n

	def findKthNode(self, head, k):
		prev = None
		tmp = head
		for i in range(1, k):
			prev = tmp
			tmp = tmp.next
		prev.next = None
		return tmp

	def findTail(self, head):
		if head == None:
			return head
		tmp = head
		while tmp.next:
			tmp = tmp.next
		return tmp

	def insertionSortList(self, head):
		if head == None or head.next == None:
			return head
		n = self.getLen(head)

		# n interations
		for k in range(2, n + 1):
			# get the ith element
			k_node = self.findKthNode(head, k)
			x = k_node.val
			prev = None
			tmp = head
			while tmp and tmp.val <= x:
				prev = tmp
				tmp = tmp.next
			if tmp == None:
				prev.next = k_node
			elif prev == None:
				nxt = k_node.next
				k_node.next = head
				self.findTail(k_node).next = nxt
				head = k_node
			else:
				nxt = k_node.next
				k_node.next = prev.next
				prev.next = k_node
				self.findTail(head).next = nxt
		return head
