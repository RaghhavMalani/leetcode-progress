class Solution:
    def bfs(self, row, col, vis, grid):
        n = len(grid)
        m = len(grid[0])
        vis[row][col] = 1
        queue = deque()
        queue.append((row, col))

        while (queue):
            row, col = queue.popleft()

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for delrow, delcol in directions:
                    nrow = row + delrow
                    ncol = col + delcol
                    if (nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and (not vis[nrow][ncol]) and grid[nrow][ncol] == "1"):
                        vis[nrow][ncol] = 1
                        queue.append((nrow,ncol))

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]

        count = 0
        for row in range(n):
            for col in range(m):
                if not vis[row][col] and grid[row][col] == "1":
                    count += 1
                    self.bfs(row, col, vis, grid)

        return count
