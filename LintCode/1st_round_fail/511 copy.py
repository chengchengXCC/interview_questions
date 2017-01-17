class Solution:
	'''
		Given 1->2->3->4->null and v1 = 2, v2 = 4.
		Return 1->4->3->2->null.
	'''
	# Time Complexity: 
	def containsV(self, head, v1, v2):
		tmp = head
		flag = 0
		while tmp:
			if tmp.val == v1 or tmp.val == v2:
				flag += 1
				if tmp.next:
					tmp.next.val == v1 or tmp.next.val == v2:
					flag += 1
			tmp = tmp.next
		return flag

    def swapNodes(self, head, v1, v2):
		if head == None or v1 == v2:
			return head
		if self.containsV(head, v1, v2) < 2:
			return head

		# v1 and v2 are not adjacent
		if self.containsV(head, v1, v2) == 2:
			prev1 = None
			node1 = None
			prev2 = None
			node2 = None
			prev = None
			tmp = head
			# find node1
			while tmp:
				if tmp.val == v1 or tmp.val == v2:
					prev1 = prev
					node1 = tmp
					break
				prev = tmp
				tmp = tmp.next
			prev = None
			tmp = node1.next
			while tmp:
				if tmp.val == v1 or tmp.val == v2:
					prev2 = prev
					node2 = tmp
					break
				prev = tmp
				tmp = tmp.next
			

		# v1 and v2 are adjacent
		else:



