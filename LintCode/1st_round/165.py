class Solution:
	# Time Complexity: O(n1+n2)
	def mergeTwoLists(self, l1, l2):
		dummy = ListNode(-1)
		tmp = dummy
		tmp1 = l1
		tmp2 = l2
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
		