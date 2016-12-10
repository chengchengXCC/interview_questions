#!/usr/bin/python

import requests
import pdb
import sys

class Solution:
	def findTail(self, head):
		tmp = head
		while tmp.next:
			tmp = tmp.next
		return tmp

	def partition(self, head, x):
	 	small_dummy = ListNode(-1)
	 	small_tmp = small_dummy
	 	big_dummy = ListNode(-1)
	 	big_tmp = big_dummy
	 	tmp = head
	 	while tmp:
	 		if tmp.val < x:
	 			small_tmp.next = tmp
	 			small_tmp = small_tmp.next
	 		else:
	 			big_tmp.next = tmp
	 			big_tmp = big_tmp.next
	 		tmp = tmp.next
	 	small_tmp.next = None
	 	big_tmp.next = None
	 	self.findTail(small_dummy).next = big_dummy.next
	 	return small_dummy.next

