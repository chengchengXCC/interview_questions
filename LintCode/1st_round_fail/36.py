class Solution:	
    # Given 1->2->3->4->5->NULL, m = 2 and n = 4, return 1->4->3->2->5->NULL.
    def reverse(self, head):
        prev = None
        tmp = head
        while tmp:
            nxt = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = nxt
        return prev

    def findTail(self, head):
        if head == None:
            return head
        tmp = head
        while tmp.next:
            tmp = tmp.next
        return tmp

    def reverseBetween(self, head, m, n):
        # locate mth node and its predecessor
        prev_m_node = None
        m_node = tmp
        for i in range(1, m):
            prev_m_node = tmp
            m_node = m_node.next
        # locate nth node and its sucessor
        n_node = head
        succ_n_node = None
        for i in range(1, n):
            n_node = n_node.next
        succ_n_node = n_node.next

        prev_m_node.next = None
        n_node.next = None
        tmp_head = self.reverse(m_node)
        tail = self.findTail(tmp_head)
        if prev_m_node:
            prev_m_node.next = tmp_head
        tail.next = succ_n_node
        if prev_m_node:
            return head
        else:
            return tmp_head






