"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        self.left, self.right = None, None
"""

class Solution:	
    # @param root, start, end: The root of segment tree and 
    #                          an segment / interval
    # @return: The count number in the interval [start, end] 
    def query(self, root, start, end):
        # write your code here
        result = 0
        if root == None:
            return result
        while start <= end:
            prev = None
            tmp = root
            while tmp:
                #print tmp.start, tmp.end
                if start == tmp.start and tmp.end <= end:
                    start = tmp.end + 1
                    result += tmp.count
                    break
                elif start <= tmp.start and tmp.end == end:
                    end = tmp.start - 1
                    result += tmp.count
                    break
                else:
                    prev = tmp
                    if end > (tmp.start + tmp.end) / 2:
                        tmp = tmp.right
                    else:
                        tmp = tmp.left
            if tmp == None:
                end = prev.end
        return result
                
                    
                
                
                
                    