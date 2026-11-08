class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        row_count = [0] * m
        col_count = [0] * n

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    row_count[r] += 1
                    col_count[c] += 1

        ans = 0

        for r in range(m):
            for c in range(n):
                if (
                    grid[r][c] == 1
                    and (row_count[r] > 1 or col_count[c] > 1)
                ):
                    ans += 1

        return ans
        