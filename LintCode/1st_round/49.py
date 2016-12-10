class Solution:
    '''
    For "abAcD", a reasonable answer is "acbAD"
    '''
    def isLower(self, char):
        if char >= 'a' and char <= 'z':
            return True
        else:
            return False

    def swap(self, chars, i, j):
        tmp = chars[i]
        chars[i] = chars[j]
        chars[j] = tmp

    # Time Complexity: O(N)
    def sortLetters(self, chars):
        if chars == None or len(chars) == 0:
            return chars
        start = 0
        end = len(chars)
        while start < end:
            while start < end and self.isLower(chars[start]):
                start += 1
            while start < end and not self.isLower(chars[end]):
                end -= 1
            if start < end:
                self.swap(chars, start, end)
                start += 1
                end -= 1



  