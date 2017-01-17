#!/usr/bin/python

class Solution:
    # Time Complexity: O(N)
    def swapPairs(self, head):
        dummy = ListNode(-1)
        tmp = dummy
        while tmp.next and tmp.next.next:
            new_node = tmp.next.next.next
            nxt = tmp.next
            nxtnxt = tmp.next.next
            tmp.next = nxtnxt
            tmp.next.next = nxt
            tmp.next.next.next = new_node
            tmp = nxt
        return dummy.next
		