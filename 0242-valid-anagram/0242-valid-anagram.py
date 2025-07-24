class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False

        counts = {}
        countt = {}

        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i],0) + 1
            countt[t[i]] = countt.get(t[i],0) + 1

        return counts == countt 