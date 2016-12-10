class Solution:	
    '''
    Given 1->2->3->3->4->4->5, return 1->2->5.
    Given 1->1->1->2->3, return 2->3. 
    '''
    def deleteDuplicates(self, head):
        if head == None:
            return head
        dict = {}
        tmp = head
        while tmp:
            if tmp.val not in dict:
                dict[tmp.val] = 1
            else:
                dict[tmp.val] = dict[tmp.val] + 1
            tmp = tmp.next
        dummyHead = ListNode(-1)
        dummyHead.next = head
        tmp = dummyHead
        cur = head
        while cur:
            if dict[cur.val] > 1:
                tmp.next = tmp.next.next
                cur = cur.next
            else:
                tmp = tmp.next
                cur = cur.next
        return dummyHead.next




