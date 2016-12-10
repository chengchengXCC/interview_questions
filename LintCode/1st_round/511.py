import pdb

class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

class Solution:	
    '''
        Given 1->2->3->4->null and v1 = 2, v2 = 4.
        Return 1->4->3->2->null.
    '''
    def constructList(self, nums):
        dummy = ListNode(-1)
        tmp = dummy
        for i in range(0, len(nums)):
            tmp.next = ListNode(nums[i])
            tmp = tmp.next
        return dummy.next

    def printList(self, head):
        tmp = head
        s = ""
        while tmp:
            s = s + " " + str(tmp.val)
            tmp = tmp.next
        print s

    def hasBothNodes(self, head, v1, v2):
        tmp = head
        count = 0
        while tmp:
            if tmp.val == v1 or tmp.val == v2:
                count += 1
            tmp = tmp.next
        return count

    def getTail(self, head):
        tmp = head
        while tmp.next:
            tmp = tmp.next
        return tmp

    def swapNodes(self, head, v1, v2):
        if head == None or v1 == v2:
            return head
        if self.hasBothNodes(head, v1, v2) < 2:
            return head
        l1 = None
        node1 = None
        l2 = None
        node2 = None
        l3 = None
        prev = None
        tmp = head
        # get l1 and node1
        while tmp and tmp.val != v1 and tmp.val != v2:
            prev = tmp
            tmp = tmp.next
        if prev:
            prev.next = None
            l1 = head
        node1 = tmp
        tmp = tmp.next
        node1.next = None
        new_head = tmp
        prev = None
        # get l2 and node2
        while tmp and tmp.val != v1 and tmp.val != v2:
            prev = tmp
            tmp = tmp.next
        if prev:
            prev.next = None
            l2 = new_head
        node2 = tmp
        tmp = tmp.next
        node2.next = None
        l3 = tmp
        dummy = ListNode(-1)
        dummy.next = l1
        self.getTail(dummy).next = node2
        node2.next = l2
        self.getTail(dummy).next = node1
        node1.next = l3
        return dummy.next

if __name__ == '__main__':
    s = Solution()
    head = s.constructList([1,2,3,4])
    s.printList(s.swapNodes(head, 2, 4))






        