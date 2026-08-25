class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        maxLen = 1

        def expand(left, right):
            nonlocal start, maxLen

            while left >= 0 and right < len(s) and s[left] == s[right]:
                length = right - left + 1

                if length > maxLen:
                    maxLen = length
                    start = left

                left -= 1
                right += 1

        for i in range(len(s)):

            expand(i, i)
            expand(i, i + 1)

        return s[start:start + maxLen]