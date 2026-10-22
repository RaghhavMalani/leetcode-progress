class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        INF = float('inf')
        ans = INF

        increasing = True

        for i in range(n):
            if nums[i] != (nums[0] + i) % n:
                increasing = False
                break

        if increasing:
            k = nums[0]
            if k == 0:
                ans = 0
            else:
                ans = min(ans, n - k, k + 2)

        decreasing = True

        for i in range(n):
            if nums[i] != (nums[0] - i) % n:
                decreasing = False
                break

        if decreasing:
            k = (n - 1 - nums[0]) % n

            ans = min(ans, min(k, n - k) + 1)

        return -1 if ans == INF else ans