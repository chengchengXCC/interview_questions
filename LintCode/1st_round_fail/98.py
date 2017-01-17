#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
	# sol1: merge sort
	'''
	def findMid(self, head):
		n = 0
		tmp = head
		while tmp:
			tmp = tmp.next
			n += 1
		n = n/2
		prev = None
		for i in range(0, n):
			prev = tmp
			tmp = tmp.next
		prev.next = None
		return tmp

	def merge(self, head1, head2):
		dummy_head = ListNode(-1)
		tmp = dummy_head
		tmp1 = head1
		tmp2 = head2
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
		return dummy_head.next
		
	def mergeSort(self, head):
		if head == None or head.next == None:
			return head
		head_2 = self.findMid(head)
		return self.merge(self.mergeSort(head), self.mergeSort(head_2))

	def sortList(self, head):
		if head == None or head.next == None:
			return head
		return mergeSort(head)
	'''

	# sol2: quickSort
	def findMid(self, head):
		n = 0
		tmp = head
		while tmp:
			tmp = tmp.next
			n += 1
		n = n/2
		tmp = head
		for i in range(0, n):
			tmp = tmp.next
		return tmp

	def combine(self, left, right):
		if left == None:
			return right
		if right == None:
			return left
		left_tail = left
		while left_tail.next:
			left_tail = left_tail.next
		left_tail.next = right
		return left

	def quickSort(self, head):
		if head == None or head.next == None:
			return head
		mid = self.findMid(head)
		left_dummy = ListNode(-1)
		left_tmp = left_dummy
		right_dummy = ListNode(-1)
		right_tmp = right_dummy
		middle_dummy = ListNode(-1)
		middle_tmp = middle_dummy
		tmp = head
		while tmp:
			if tmp.val < mid.val:
				left_tmp.next = tmp
				left_tmp = left_tmp.next
			elif tmp.val > mid.val:
				right_tmp.next = tmp
				right_tmp = right_tmp.next
			else:
				middle_tmp.next = tmp
				middle_tmp = middle_tmp.next
			tmp = tmp.next
		left_tmp.next = None
		right_tmp.next = None
		middle_tmp.next = None
		left = self.quickSort(left_dummy.next)
		right = self.quickSort(right_dummy.next)
		return self.combine(self.combine(left, middle_dummy.next), right)

	def sortList(self, head):
		if head == None or head.next == None:
			return head
		return self.quickSort(head)