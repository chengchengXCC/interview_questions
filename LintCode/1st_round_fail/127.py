import Queue

# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution:
	"""
	@param graph: A list of Directed graph node
	@return: A list of graph nodes in topological order.
	"""
	# BFS
	'''
	def topSort(self, graph):
		# write your code here
		if graph == None:
			return []
		dict = {}
		q = Queue.Queue()
		result = []
		# step1: calcualte in-degreee
		for node in graph:
			for item in node.neighbors:
				if item in dict:
					dict[item] += 1
				else:
					dict[item] = 1
		
		# step2: put node with 0 in-degree into q, and result
		for node in graph:
			if node in dict:
				q.put(node)
				result.append(node)
		# step3:
		while not q.empty():
			node = q.get()
			for item in node.neighbors:
				dict[item] -= 1
				if dict[item] == 0:
					q.put(item)
					result.append(item)
		return result
		'''

		# DFS
		def dfs(self, node, ans, dict):
			# append this 0 in-degree node
			ans.append(node)
			dict[node] -= 1
			# for each neigbour of current node, in-degree --
			for item in node.neighbors:
				dict[item] -= 1
				if dict[item] == 0:
					self.dfs(item, ans, dict)

		def topSort(self, graph):
			if graph == None:
				return []
			dict = {}
			# get in-degree of each node (including 0 in-degree)
			for node in graph:
				dict[node] = 0
				for item in node.neighbors:
					if item in dict:
						dict[item] += 1
					else:
						dict[item] = 1
			# from each node with 0 in-degree, we do DFS traversal
			ans = []
			for node in graph:
				if dict[node] == 0:
					self.dfs(node, ans, dict)
			return ans












