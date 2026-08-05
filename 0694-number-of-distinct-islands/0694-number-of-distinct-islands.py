class Solution:
    def dfs(self, row, col, grid, vis, base_vector, row0, col0):
        vis[row][col] = 1
        n = len(grid)
        m = len(grid[0])
        base_vector.append((row - row0, col - col0))
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        for (drow, dcol) in directions:
            nrow = row + drow
            ncol = col + dcol
            if (nrow >= 0 and ncol >= 0 and nrow < n and ncol < m and vis[nrow][ncol]== 0 and grid[nrow][ncol] == 1):
                self.dfs(nrow, ncol, grid, vis, base_vector, row0, col0)


    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        vis = [[0 for _ in range(m)] for _ in range(n)]
        storage = set()

        for row in range(n):
            for col in range(m):
                if (not vis[row][col]) and grid[row][col] == 1:
                    base_vector = []
                    self.dfs(row, col, grid, vis, base_vector, row, col)
                    storage.add(tuple(base_vector))
        return len(storage)