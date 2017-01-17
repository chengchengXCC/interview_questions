class Solution:	
    '''
    Given 1->2->1, return true
    '''
    def reverse(self, head):
        if head == None or head.next:
            return head
        prev = None
        tmp = head
        while tmp:
            nxt = tmp.next
            tmp.next = prev
            prev = tmp 
            tmp = nxt
        return prev

    def isPalindrome(self, head):
        if head == None or head.next == None:
            return True
        slow = head
        fast = head.next
        while fast:
            if fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            else:
                break
        l1 = head
        l2 = slow.next
        slow.next = None
        l2 = self.reverse(l2)
        tmp1 = l1
        tmp2 = l2
        while tmp1 and tmp2:
            if tmp1.val != tmp2.val:
                return False
            tmp1 = tmp1.next
            tmp2 = tmp2.next
        return True



       

                
                
                
                    