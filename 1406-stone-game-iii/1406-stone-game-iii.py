class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 3)

        for i in range(n - 1, -1, -1):
            current_sum = 0
            dp[i] = float("-inf")

            for take in range(3):
                if i + take >= n:
                    break

                current_sum += stoneValue[i + take]
                difference = current_sum - dp[i + take + 1]
                dp[i] = max(dp[i], difference)

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
        