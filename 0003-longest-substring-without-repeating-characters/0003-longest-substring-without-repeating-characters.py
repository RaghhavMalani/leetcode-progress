class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s1 = set()
        l = 0 
        res = 0

        for r in range(len(s)):
            while s[r] in s1:
                s1.remove(s[l])
                l = l + 1
            
            s1.add(s[r])
            res = max(res, r - l + 1)

        return res
