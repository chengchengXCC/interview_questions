from Queue import PriorityQueue
class Solution:	
    '''
    Given "abcdefg"
    offset=0 => "abcdefg"
    offset=1 => "gabcdef"
    offset=2 => "fgabcde"
    offset=3 => "efgabcd"
    '''
    # Sol1: Divide and Conque
    # Time: n * log N
    '''
    def merge2(self, array1, array2):
        if array1 == None:
            return array2
        if array2 == None:
            return array1
        i = j = 0
        new_array = []
        while i < len(array1) and j < len(array2):
            if array1[i] < array2[j]:
                new_array.append(array1[i])
                i += 1
            else:
                new_array.append(array2[j])
                j += 1
        while i < len(array1):
            new_array.append(array1[i])
            i += 1
        while j < len(array2):
            new_array.append(array2[j])
            j += 1
        return new_array

    def helper(self, arrays, l, r):
        if l > r:
            return None
        if l == r:
            return arrays[l]
        mid = (l + r) / 2
        left = self.helper(arrays, l, mid - 1)
        right = self.helper(arrays, mid + 1, r)
        return self.merge2(left, right)

    def mergekSortedArrays(self, arrays):
        if arrays == None or len(arrays) == 0:
            return []
        return self.helper(arrays, 0, len(arrays) - 1)
    '''

    # Sol2: 2 2 合并(略)
    # Sol3: priority queue
    def mergekSortedArrays(self, arrays):
        if arrays == None or len(arrays) == 0:
            return []
        result = []
        pq = PriorityQueue()
        for i in range(0, len(arrays)):
            pq.put((arrays[i][0], i, 0))
        while not pq.empty():
            item = pq.get()
            result.put(item[0])
            if item[2] < len(arrays[item[1]]) - 1:
                pq.put((arrays[item[1]][item[2] + 1], item[1], item[2] + 1))
        return result







        