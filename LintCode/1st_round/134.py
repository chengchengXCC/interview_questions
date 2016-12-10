'''
class LinkNode:
	def __init__(self, key=None, value=None, next=None):
		self.key = key
		self.val = value
		self.next = next

class LRUCache:
	# @param capacity, an integer
	def __init__(self, capacity):
		# write your code here
		self.capacity = capacity
		self.size = 0
		self.hash = {}
		self.dummyHead = LinkNode(-1, -1)

	# @return an integer
	def get(self, key):
		# write your code here
		if key not in self.hash or self.hash[key] == -1:
			return -1
		else:
			prev = self.dummyHead
			tmp = self.dummyHead.next
			value = -1
			while tmp:
				if tmp.key == key:
					value = tmp.val
					if prev != self.dummyHead:
						nxt = self.dummyHead.next
						prev.next = prev.next.next
						self.dummyHead.next = tmp
						tmp.next = nxt
					break
				else:
					prev = tmp
					tmp = tmp.next
			return value

	# TODO :: 检查这段代码
	def set(self, key, value):
		# set 
		if key in self.hash and self.hash[key] != -1:
			prev = self.dummyHead
			tmp = self.dummyHead.next
			while tmp:
				if tmp.key == key:
					tmp.val = value
					if prev != self.dummyHead:
						prev.next = prev.next.next
						nxt = self.dummyHead.next
						self.dummyHead.next = tmp
						tmp.next = nxt
					break
				else:
					tmp = tmp.next
			return 

		# insert the node
		if self.size == self.capacity:
			# remove the last node
			prev = self.dummyHead
			tmp = self.dummyHead.next
			while tmp.next:
				prev = tmp
				tmp = tmp.next
			prev.next = None
			self.hash[tmp.key] = -1
			# insert the new node at head
			self.hash[key] = value
			node = LinkNode(key, value)
			nxt = self.dummyHead.next
			self.dummyHead.next = node
			node.next = nxt
		else:
			# insert the new node at the head
			self.hash[key] = value
			node = LinkNode(key, value)
			nxt = self.dummyHead.next
			self.dummyHead.next = node
			node.next = nxt
			self.size += 1
'''

class LinkedNode:    
	def __init__(self, key=None, value=None, next=None):
    	self.key = key
        self.value = value
        self.next = next


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
    	self.size = 0
    	self.hash = {}
    	self.head = LinkNode()
    	self.tail = self.head

    # insert a new node at the end
   	def push_back(self, node):
   		self.hash[node.key] = self.tail
   		self.tail.next = node
   		self.tail = node

   	# remove a node from the head
   	def pop_front(self):
   		del self.hash[self.head.next.key]
   		self.head.next = self.head.next.next
   		self.hash[self.head.next.key] = self.head

   	# change "prev->node->next...->tail"
    # to "prev->next->...->tail->node"
   	def kick(self, prev):
   		node = prev.next
   		if node == self.tail:
   			return
   		prev.next = prev.next.next
   		self.hash[prev.next.key] = prev
   		self.push_back(node)

   	def get(self, key):
   		if key not in self.hash:
   			return -1
   		prev = self.hash[key]
   		node = prev.next
   		if node != self.tail:
   			self.kick(prev)
   		return value

   	def set(self, key, value):
   		if key in self.hash:
   			prev = self.hash[key]
   			node = prev.next
   			node.val = value
   			if node != self.tail:
   				self.kick(node)
   		else:
   			if self.size == self.capacity:
   				self.push_back(LinkNode(key, value))
   				self.pop_front()
   			else:
   				self.push_back(LinkNode(key, value))






