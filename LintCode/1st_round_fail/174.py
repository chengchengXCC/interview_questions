class Solution:	
    '''
    Given linked list: 1->2->3->4->5->null, and n = 2.
    After removing the second node from the end, the linked list becomes 1->2->3->5->null.
    '''
    # 时间复杂度： O(N)
    # 空间复杂度： O(1)
    def removeNthFromEnd(self, head, n):
        if head == None:
            return None
        fast = head
        for i in range(0, n):
            if fast == None:
                return head
            fast = fast.next
        prev = None
        slow = head
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        if prev == None:
            return head.next
        prev.next = prev.next.next
        return head



