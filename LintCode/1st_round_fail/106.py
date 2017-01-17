class Solution: 
    '''
    Given a singly linked list where elements are sorted in ascending order
    , convert it to a height balanced BST.
                   2
    1->2->3  =>   / \
                 1   3
    '''
    #这道题目在做的时候函数多处忘了写返回值
    def getLen(self, head):
        #时间复杂度：O(n)
        tmp = head
        n = 0
        while tmp:
            n += 1
            tmp = tmp.next
        return n

    def findMid(self, head):
        # 时间复杂度：O(n)
        # len(head) >= 2
        # result contains prev Node of mid node, and mid Node
        result = []
        n = self.getLen(head)
        n = n / 2
        prev = None
        mid = head
        for i in range(0, n):
            prev = mid
            mid = mid.next
        result.append(prev)
        result.append(mid)
        return result

    def helper(self, head):
    # 时间复杂度：N*O(log(N))
        if head == None:
            return None
        if head.next == None:
            return TreeNode(head.val)
        result = self.findMid(head)
        result[0].next = None
        left_list = head
        right_list = result[1].next
        node = TreeNode(result[1].val)
        node.left = self.helper(left_list)
        node.right = self.helper(right_list)
        return node

    def sortedListToBST(self, head):
        if head == None:
            return None
        return self.helper(head)