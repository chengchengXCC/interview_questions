import Queue

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:

	# Sol1: recursive
	'''
	def __init__(self):
		self.dict = {}
		
	def cloneGraph(self, node):
		# write your code here
		if node == None:
		    return None
		if node.label in self.dict:
			return self.dict[node.label]
		else:
			root = UndirectedGraphNode(node.label)
			self.dict[node.label] = root
			for item in node.neighbors:
				root.neighbors.append(self.cloneGraph(item))
			return root
	'''
	def __init__(self):
		self.dict = {}
		
	def BFS(self, node):
		result = []
		dict = {}
		q = Queue.Queue()
		result.append(node)
		q.put(node)
		dict[node] = 1
		while not q.empty():
			tmp = q.get()
			for item in tmp.neighbors:
			   	if item not in dict:
			   		dict[item] = 1
			   		q.put(item)
			   		result.append(item)
		return result

	def cloneGraph(self, node):
		if node == None:
			return None
		# step1: get all nodes from node using BFS
		nodes = self.BFS(node)
		# create old-node -- new-node (1-to-1 mapping)
		for old_node in nodes:
			self.dict[old_node] = UndirectedGraphNode(old_node.label)
		# get neigbours information
		for old_node in nodes:
			for item in old_node.neighbors:
				self.dict[old_node].neighbors.append(self.dict[item])
		return self.dict[node]