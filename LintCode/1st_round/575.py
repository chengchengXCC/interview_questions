import sys

class Solution:	
    '''
    s = 3[2[ad]3[pf]]xyz, return adadpfpfpfadadpfpfpfadadpfpfpfxyz
    '''
    # Sol1: Recursion
    '''
    def hasDigit(self, s):
        result = [] 
        for i in range(0, len(s)):
            if s[i].isdigit():
                result.append(i)
                while i < len(s):
                    if s[i].isdigit():
                        i += 1
                    else:
                        result.append(i - 1)
                        return result
        result.append(-1)
        result.append(-1)
        return result

    def findEndBracket(self, s):
        k = 1
        i = s.find('[')
        i += 1
        while i < len(s):
            if s[i] == '[':
                k += 1
            elif s[i] == ']':
                if k == 1:
                    return i
                else:
                    k -= 1
            i += 1
        return -1

    def helper(self, s):
        result = self.hasDigit(s)
        if s == None or len(s) == 0 or result[0] == -1 and result[1] == -1:
            return s
        #print result
        s1 = s[0 : result[0]]
        n1 = int(s[result[0] : result[1] + 1])
        j = self.findEndBracket(s)
        s2 = s[result[1] + 2 : j]
        s3 = s[j + 1 : ]
        #print "s2", s2
        s2 = self.helper(s2)
        #print "s3", s3
        s3 = self.helper(s3)
        new_s2 = ""
        for i in range(0, n1):
            new_s2 = new_s2 + s2
        return s1 + new_s2 + s3

    def expressionExpand(self, s):
        if s == None or len(s) == 0:
            return s
        return self.helper(s)
    '''

    def isNum(self, a):
        if a > 0 and a < sys.maxint:
            return True
        else:
            return False

    def expressionExpand(self, s):
        if s == None or len(s) == 0:
            return s
        stack = []
        while len(s) > 0:
            if s[0].isdigit():
                i1 = 0
                while i1 < len(s) and s[i1].isdigit():
                    i1 += 1
                stack.append(int(s[0 : i1]))
                s = s[i1 : ]
            elif s[0].isalpha():
                i1 = 0
                while i1 < len(s) and s[i1].isalpha():
                    i1 += 1
                stack.append((s[0 : i1]))
                s = s[i1 : ]
            elif s[0] == '[':
                s = s[1 : ]
            else:
                new_str = ""
                while stack:
                    tmp = stack.pop()
                    if self.isNum(tmp):
                        res = ""
                        for i in range(0, tmp):
                            res += new_str
                        stack.append(res)
                        s = s[1 : ]
                        break
                    else:
                        new_str = tmp + new_str
                s = s[1 : ]
        res = ""
        while stack:
            res = stack.pop() + res
        print res

if __name__ == '__main__':
    s = Solution()
    s.expressionExpand("3[2[ad]3[pf]]xyz")
                
                
                
                    