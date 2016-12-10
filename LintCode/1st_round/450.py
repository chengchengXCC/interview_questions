class Solution:	
    '''
    Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
    If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
    '''

    def getLen(self, head):
        if head == None:
            return 0
        n = 0
        tmp = head
        while tmp:
            n += 1
            tmp = tmp.next
        return n

    def findKth(self, head, k):
        tmp = head
        for i in range(1, k):
            if tmp == None:
                break
            tmp = tmp.next
        if tmp == None:
            return None
        return tmp

    def reverse(self, head):
        tail = head
        tmp = head
        prev = None
        while tmp:
            nxt = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = nxt
        result = []
        result.append(prev)
        result.append(tail)
        return result


    def reverseKGroup(self, head, k):
        n = self.getLen(head)
        if n <= k:
            return head
        dummy = ListNode(-1)
        tmp = dummy
        while True:
            node = self.findKth(head, k)
            if node == None:
                tmp.next = head
                break
            nxt = node.next
            node.next = None
            result = self.reverse(head)
            tmp.next = result[0]
            tmp = result[1]
            head = nxt
        return dummy.next





        
                
                    