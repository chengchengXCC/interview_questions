class Solution:	
    '''
    Given 6->1->7 + 2->9->5. That is, 617 + 295
    Return 9->1->2. That is, 912
    '''
    # Time complexity: O(数字的位数)
    def getNum(self, head):
        sum = 0
        tmp = head
        while tmp:
            sum = sum * 10 + tmp.val
            tmp = tmp.next
        return sum

    def addLists2(self, l1, l2):
        num1 = self.getNum(l1)
        num2 = self.getNum(l2)
        sum = num1 + num2
        if sum == 0:
            return ListNode(0)
        dummy = ListNode(-1)
        while sum > 0:
            num = sum % 10
            nxt = dummy.next
            dummy.next = ListNode(num)
            dummy.next.next = nxt
            sum = sum / 10
        return dummy.next
        