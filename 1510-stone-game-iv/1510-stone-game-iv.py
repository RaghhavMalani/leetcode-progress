class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)

        for stones in range(1, n + 1):
            x = 1

            while x * x <= stones:
                if dp[stones - x * x] == False:
                    dp[stones] = True
                    break

                x += 1

        return dp[n]