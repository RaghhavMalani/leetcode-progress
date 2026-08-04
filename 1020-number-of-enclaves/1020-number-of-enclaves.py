class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        vis = [[0 for _ in range(m)] for _ in range(n)]
        q = deque()
        for row in range(n):
            for col in range(m):
                if (row == 0 or row == n-1 or col == 0 or col == m -1):
                    if grid[row][col] == 1:
                        q.append((row,col))
                        vis[row][col] = 1

        while q:
            (ROW, COL) = q.popleft()
            directions = [(-1,0),(1,0),(0,1),(0,-1)]
            for (drow, dcol) in directions:
                nrow = ROW + drow
                ncol = COL + dcol
                if (nrow >= 0 and ncol >= 0 and nrow < n and ncol < m and vis[nrow][ncol]== 0 and grid[nrow][ncol] == 1):
                    q.append((nrow,ncol))
                    vis[nrow][ncol] = 1

        count = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1 and vis[row][col] == 0:
                    count += 1
        return count

        