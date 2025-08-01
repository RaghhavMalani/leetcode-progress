class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        count ={}
        for char in s:
            count[char] = 1 + count.get(char, 0)

        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1