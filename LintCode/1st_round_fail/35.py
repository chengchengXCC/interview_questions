class Solution:
	'''
	For linked list 1->2->3, the reversed linked list is 3->2->1
	'''
	# Time Complexity: O(N)
	def reverse(self, head):
		if head == None or head.next == None:
			return head
		prev = None
		tmp = head
		while tmp:
			nxt = tmp.next
			tmp.next = prev
			prev = tmp
			tmp = nxt
		return prev
		