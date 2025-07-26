class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        s = set(nums)
        longest = 0

        for num in s:
            if (num-1) not in s:
                length = 0
                while (length + num) in s:
                    length += 1
                longest = max(longest, length)

        return longest