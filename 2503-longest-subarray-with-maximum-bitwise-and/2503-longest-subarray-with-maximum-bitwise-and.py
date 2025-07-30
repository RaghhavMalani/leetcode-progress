class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        size = 0
        res = 0
        curmax = 0
        for n in nums:
            if n > curmax:
                curmax = n
                size = 1
                res = 0
            elif n == curmax:
                size += 1
            else:
                size = 0
            
            res = max(size, res)
        
        return res