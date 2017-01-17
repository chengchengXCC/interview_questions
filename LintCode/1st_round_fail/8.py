class Solution:	
    '''
    Given "abcdefg"
    offset=0 => "abcdefg"
    offset=1 => "gabcdef"
    offset=2 => "fgabcde"
    offset=3 => "efgabcd"
    '''
    def reverse(self, s, start, end):
        while start < end:
            tmp = s[start]
            s[start] = s[end]
            s[end] = tmp
            start += 1
            end -= 1

    def rotateString(self, s, offset):
        if s == None or len(s) == 0:
            return s
        offset = offset % len(s)
        self.reverse(s, 0, len(s) - 1 - offset)
        self.reverse(s, len(s) - offset, len(s) - 1)
        self.reverse(s, 0, len(s) - 1)

       

                
                
                
                    