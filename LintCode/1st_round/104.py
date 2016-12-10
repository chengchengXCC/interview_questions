#!/usr/bin/python
from Queue import PriorityQueue

class Solution:
	# sol1: Priority Queue
	'''
	def mergeKLists(self, lists):
		# number of list within lists: n
		# average length of each list: m
		if lists == None or len(lists) == 0:
			return None
		dummy = ListNode(-1)
		tmp = dummy
		pq = PriorityQueue()
		# k*log(k)
		for list in lists:
			if list:
				pq.put((list.val, list))
		# km*Log(k)
		while not pq.empty():
			node = pq.get()
			tmp.next = node[1]
			tmp = tmp.next
			if node[1].next:
				pq.put((node[1].next.val, node[1].next))
		return dummy.next
	'''

	# merge 2 list
	# O(M+N)
	'''
	def merge2(self, list1, list2):
		if list1 == None:
			return list2
		if list2 == None:
			return list1
		dummy = ListNode(-1)
		tmp = dummy
		tmp1 = list1
		tmp2 = list2
		while tmp1 and tmp2:
			if tmp1.val < tmp2:
				tmp.next = tmp1
				tmp1 = tmp1.next
			else:
				tmp.next = tmp2
				tmp2 = tmp2.next
			tmp = tmp.next
		if tmp1:
			tmp.next = tmp1
		if tmp2:
			tmp.next = tmp2
		return dummy.next

	# NLOG(N)
	def mergeKLists_helper(self, lists, i, j):
		if i == j:
			return lists[i]
		mid = (i + j) / 2
		left = self.mergeKLists_helper(lists, i, mid)
		right = self.mergeKLists_helper(lists, mid + 1, j)
		return self.merge2(left, right)

	def mergeKLists(self, lists):
		if lists == None or len(lists) == 0:
			return None
		return self.mergeKLists_helper(lists, 0, len(lists) - 1)
	'''

	# merge 2 by 2
	# O(M+N)
	def merge2(self, list1, list2):
		if list1 == None:
			return list2
		if list2 == None:
			return list1
		dummy = ListNode(-1)
		tmp = dummy
		tmp1 = list1
		tmp2 = list2
		while tmp1 and tmp2:
			if tmp1.val < tmp2.val:
				tmp.next = tmp1
				tmp1 = tmp1.next
			else:
				tmp.next = tmp2
				tmp2 = tmp2.next
			tmp = tmp.next
		if tmp1:
			tmp.next = tmp1
		if tmp2:
			tmp.next = tmp2
		return dummy.next

	def mergeKLists(self, lists):
		if lists == None or len(lists) == 0:
			return None
		result = lists[0]
		# len(lists) * O(MN)
		for i in range(0, len(lists) - 1):
			result = self.merge2(result, lists[i + 1])
		return result














			