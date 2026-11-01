class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7

        m = len(grid)
        n = len(grid[0])

        down = [0] * n
        down[0] = 1

        for r in range(m):
            right = 0

            for c in range(n):
                if grid[r][c] == 0:
                    total = (right + down[c]) % MOD
                    right = total
                    down[c] = total
                else:
                    right, down[c] = down[c], right

        return right