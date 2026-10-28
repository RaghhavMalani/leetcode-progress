class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # dp[j] = all XOR values that can reach current row, column j
        dp = [set() for _ in range(n)]

        for r in range(m):
            for c in range(n):
                prev = set()

                # Starting cell
                if r == 0 and c == 0:
                    prev.add(0)

                # From above
                if r > 0:
                    prev.update(dp[c])

                # From left
                if c > 0:
                    prev.update(dp[c - 1])

                # Include current cell in XOR
                dp[c] = {
                    x ^ grid[r][c]
                    for x in prev
                }

        return min(dp[n - 1])