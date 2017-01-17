import math
import pdb

class Solution:

    def hash(self, str):
        if str == None or len(str) == 0:
            return 0
        hash = 0
        a = 378551
        b = 63689
        dict = [0 for i in range(26)]
        result = 0
        for c in str:
            dict[ord(c) - ord('a')] += 1
        for num in dict:
            hash = hash * a + num
            a = a * b
        return hash

    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        result = []
        hash_map = {}
        for str in strs:
            key = self.hash(str)
            if key not in hash_map:
                hash_map[key] = [str]
            else:
                hash_map[key].append(str)
        for key in hash_map:
            if len(hash_map[key]) > 1:
                for str in hash_map[key]:
                    result.append(str)
        return result

if __name__ == '__main__':
    s = Solution()
    print s.anagrams(["", "b", ""])
