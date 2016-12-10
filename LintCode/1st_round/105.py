class Solution:         
    # sol1:          
    # 相对于原来的list：1(1)->2(1)->3(1)->4(1)->null
    # 建立同样数值的新的list: 1(2)->2(2)->3(2)->null, 并且保持着map,存有<old_node, new_node>的信息
    # 然后创建新的list当中的random pointer。比如我们想知道1(2)的random指向哪里: 1(2).random = map.get(1(1).random)
    # 时间复杂度： O(n)
    # 空间复杂度： 除了deepcopy花费的O(n)以外。还花费了O(N)的空间存储了一个map 
    '''
    def copyRandomList(self, head):
        if head == None:
            return None
        dict = {}
        tmp1 = head
        dummy = RandomListNode(-1)
        tmp2 = dummy
        while tmp1:
            new_node = RandomListNode(tmp1.label)
            dict[tmp1] = new_node
            tmp2.next = new_node
            tmp1 = tmp1.next
            tmp2 = tmp2.next
        tmp1 = head
        while tmp1:
            if tmp1.random:
                dict[tmp1].random = dict[tmp1.random]
            else:
                dict[tmp1].random = None
            tmp1 = tmp1.next
        return dummy.next
    '''
  
    # sol2: 这个算法相对于第一种算法，空间复杂度得到了提高，达到了O(1)
    # 时间复杂度保持了 O(N)
    def copyRandomList(self, head):
        if head == None:
            return None
        tmp1 = head
        dummy = RandomListNode(-1)
        tmp2 = dummy
        while tmp1:
            nxt = tmp1.next
            new_node = RandomListNode(tmp1.label)
            tmp1.next = new_node
            new_node.random = tmp1
            tmp2.next = new_node
            tmp1 = nxt
            tmp2 = tmp2.next
        tmp2 = dummy.next
        while tmp2:
            if tmp2.random.random:
                tmp2.random = tmp2.random.random.next
            else:
                tmp2.random = None
            tmp2 = tmp2.next
        return dummy.next


