class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # Already sorted
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0

        # If length = 2 and unsorted,
        # the only useful substring is the whole string,
        # which is not allowed
        if n == 2:
            return -1

        mn = min(s)
        mx = max(s)

        # One operation
        if s[0] == mn or s[-1] == mx:
            return 1

        # Two operations
        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                return 2

        return 3