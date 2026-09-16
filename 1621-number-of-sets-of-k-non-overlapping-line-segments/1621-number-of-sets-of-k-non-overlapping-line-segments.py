class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        dp = [[0] * (k + 1) for _ in range(n)]
        pref = [[0] * (k + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1

            if i == 0:
                pref[i][0] = 1
            else:
                pref[i][0] = pref[i - 1][0] + 1

        for j in range(1, k + 1):
            for i in range(n):
                if i > 0:
                    dp[i][j] = dp[i - 1][j]

                if i > 0:
                    dp[i][j] += pref[i - 1][j - 1]

                dp[i][j] %= MOD

                if i == 0:
                    pref[i][j] = dp[i][j]
                else:
                    pref[i][j] = (pref[i - 1][j] + dp[i][j]) % MOD

        return dp[n - 1][k]