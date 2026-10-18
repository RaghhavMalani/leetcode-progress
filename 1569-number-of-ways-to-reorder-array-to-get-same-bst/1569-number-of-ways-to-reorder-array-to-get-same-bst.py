import sys
sys.setrecursionlimit(3000)

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact[n] = pow(fact[n], MOD - 2, MOD)

        for i in range(n, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def nCr(n, r):
            return (
                fact[n] *
                inv_fact[r] %
                MOD *
                inv_fact[n - r]
            ) % MOD

        def dfs(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]

            left = []
            right = []

            for x in arr[1:]:
                if x < root:
                    left.append(x)
                else:
                    right.append(x)

            left_ways = dfs(left)
            right_ways = dfs(right)

            L = len(left)
            R = len(right)

            combine = nCr(L + R, L)

            return combine * left_ways % MOD * right_ways % MOD
        return (dfs(nums) - 1) % MOD