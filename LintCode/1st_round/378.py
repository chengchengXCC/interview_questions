class Solution:	
    '''
     traverse the tree using in-order, and add node to end
    '''
    def helper(self, root, prev):
        if root == None:
            return
        self.helper(root.left. prev)
        # do sth
        node = DoublyListNode(root.val)
        prev[0].next = node
        node.prev = prev[0]
        prev[0] = node
        self.helper(root.roght, prev)
        
    def bstToDoublyList(self, root):
        head = DoublyListNode(-1)
        prev = []
        prev.append(head)
        self.helper(root, prev)
        return head.next
