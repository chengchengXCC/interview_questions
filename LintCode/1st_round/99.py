#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
	def findMid(self, head):
		n = 0
		tmp = head
		while tmp:
			n += 1
			tmp = tmp.next
		n = n/2
		tmp = head
		prev = None
		for i in range(0, n):
			prev = tmp
			tmp = tmp.next
		if prev:
			prev.next = None
		return tmp

	def reverse(self, head):
		prev = None
		tmp = head
		while tmp:
			nxt = tmp.next
			tmp.next = prev
			prev = tmp
			tmp = nxt
		return prev

	def reorderList(self, head):
		if head == None or head.next == None:
			return head
		mid = self.findMid(head)
		#if mid == head:
		#	return head
		new_head = self.reverse(mid)
		dummy_head = ListNode(-1)
		tmp = head
		new_tmp = new_head
		dummy_tmp = dummy_head
		while tmp and new_tmp:
			dummy_tmp.next = tmp
			tmp = tmp.next
			dummy_tmp = dummy_tmp.next
			dummy_tmp.next = new_tmp
			new_tmp = new_tmp.next
			dummy_tmp = dummy_tmp.next
		dummy_tmp.next = new_tmp
		return dummy_head.next







