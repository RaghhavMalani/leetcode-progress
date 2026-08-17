class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        if n == 1:
            return 0

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

        leftBest = [[0] * n for _ in range(n)]
        rightBest = [[0] * n for _ in range(n)]

        for i in range(n):
            leftBest[i][i] = stoneValue[i]
            rightBest[i][i] = stoneValue[i]

        for length in range(2, n + 1):

            for i in range(n - length + 1):

                j = i + length - 1
                target = (prefix[i] + prefix[j + 1]) // 2

                t = bisect_right(prefix, target, i + 1, j + 1 ) - 1

                best = 0

                if t >= i + 1:
                    best = max( best, leftBest[i][t - 1] )

                if t + 1 <= j:
                    best = max( best, rightBest[t + 1][j] )

                if ( t >= i + 1 and 2 * prefix[t] == prefix[i] + prefix[j + 1]):
                    best = max( best, rightBest[t][j] )

                dp[i][j] = best

                intervalSum = prefix[j + 1] - prefix[i]

                leftBest[i][j] = max( leftBest[i][j - 1], dp[i][j] + intervalSum )

                rightBest[i][j] = max( rightBest[i + 1][j], dp[i][j] + intervalSum )

        return dp[0][n - 1]