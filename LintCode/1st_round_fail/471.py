import heapq

class Node:
    def __init__(self, _value, _key):
        self.value = _value
        self.key = _key
    def __cmp__(self, other):
        if self.value != other.value:
            return self.value - other.value
        else:
            if self.key > other.key:
                return -1
            else:
                return 1

class Solution:
    # @param {string[]} words a list of string
    # @param {int} k an integer
    # @return {string[]} a list of string
    '''
    # Time complexity: nlog(n)
    def topKFrequentWords(self, words, k):
        result = []
        dict = {}
        pq = PriorityQueue()
        for word in words:
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
        for key in dict:
            pq.put((-dict[key], key))
        for i in range(0, k):
            result.put(pq.get()[1])
        return result
    '''

    def topKFrequentWords(self, words, k):
        q = []
        result = []
        dict = {}
        for word in words:
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
        for key in dict:
            if len(q) < k:
                heapq.heappush(q, (dict[key], key))
            else:
                if q[0][0] < dict[key]:
                    heapq.heappop(q)
                    heapq.heappush(q, (dict[key], key))
        while len(q) > 0:
            node = heapq.heappop(q)
            result.append(Node(node[0], node[1]))
        result.reverse()
        new_result = []
        for i in range(0, len(result)):
            new_result.append(result[1])
        return new_result







        