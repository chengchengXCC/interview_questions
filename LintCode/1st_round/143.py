class Solution:
    """
    Given colors=[3, 2, 2, 1, 4], k=4, your code should sort colors in-place 
    to [1, 2, 2, 3, 4].
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def swap(self, colors, i, j):
        tmp = colors[i]
        colors[i] = colors[j]
        colors[j] = tmp

    def sortColors2(self, colors, k):
        count = 0
        start = 0
        end = len(colors) - 1
        while count < k:
            left = start
            right = end
            min = sys.maxint
            max = -sys.maxint
            for i in range(left, right + 1):
                min = min(min, colors[i])
                max = max(max, colors[i])  
            cur = left
            while cur <= right:
                if colors[cur] == min:
                    self.swap(colors, cur, left)
                    left += 1
                    cur += 1
                elif colors[cur] > min and colors[cur] < max:
                    cur += 1
                else:
                    self.swap(colors, cur, right)
                    right -= 1
            k += 2
            start = left
            end = right





