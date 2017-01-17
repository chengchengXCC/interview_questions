from Queue import PriorityQueue
class Solution:
    '''
        Given [3,10,1000,-99,4,100] and k = 3
        Return [1000, 100, 10]
    '''
    def topk(self, nums, k):
        pq = PriorityQueue()
        for num in nums:
            pq.put(num)
        result = []
        for i in range(0, k):
            result.append(pq.get())
        return result

            