class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        @lru_cache(None)
        def dfs(r1, c1, r2):
            c2 = r1 + c1 - r2

            if (r1 >= n or c1 >= n or r2 >= n or c2 >= n or
                grid[r1][c1] == -1 or grid[r2][c2] == -1):
                return float('-inf')

            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]

            cherries = grid[r1][c1]

            if r1 != r2 or c1 != c2:
                cherries += grid[r2][c2]

            nextMove = max(
                dfs(r1 + 1, c1, r2 + 1),
                dfs(r1 + 1, c1, r2),
                dfs(r1, c1 + 1, r2 + 1),
                dfs(r1, c1 + 1, r2)
            )

            return cherries + nextMove

        ans = dfs(0, 0, 0)

        return max(0, ans)