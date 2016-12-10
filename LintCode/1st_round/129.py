"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def hashItem(self, item, new_hashTable):
    	size = len(new_hashTable)
    	val = item.val % size
    	if new_hashTable[val] == None:
    		new_hashTable[val] = ListNode(item.val)
    	else:
    		tmp = new_hashTable[val]
    		while tmp.next:
    			tmp = tmp.next
    		tmp.next = ListNode(item.val)

    def rehashing(self, hashTable):
        # write your code here
        size = len(hashTable) * 2
        new_hashTable = [None for i in range(size)]
        for item in hashTable:
        	if item:
        		tmp = item
        		while tmp:
        			self.hashItem(tmp, new_hashTable)
        			tmp = tmp.next
        return new_hashTable






