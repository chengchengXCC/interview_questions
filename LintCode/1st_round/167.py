class Solution:
	'''
	Given 7->1->6 + 5->9->2. That is, 617 + 295.
	Return 2->1->9. That is 912.
	Given 3->1->5 and 5->9->2, return 8->0->8.
	'''
	# Time Complexity: O(n)
	# n 是数字的位数
	def addLists(self, l1, l2):
		num1 = 0
		num2 = 0
		i = 1
		tmp = l1
		while tmp:
			num1 = num1 + i * tmp.val
			i = i * 10
			tmp = tmp.next
		i = 1
		tmp = l2
		while tmp:
			num2 = num2 + i * tmp.val
			i = i * 10
			tmp = tmp.next
		sum = num1 + num2
		dummy = ListNode(-1)
		tmp = dummy
		if sum == 0:
		    return ListNode(0)
		while sum > 0:
			num = sum % 10
			sum = sum / 10
			tmp.next = ListNode(num)
			tmp = tmp.next
		return dummy.next