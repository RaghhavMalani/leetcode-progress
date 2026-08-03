class Solution:
       
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        queue = deque()

        vis = [[0 for _ in range(m)] for _ in range(n)]
        count = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 2:
                    queue.append(((row, col),0))
                    vis[row][col] = 2
                else:
                    vis[row][col] = 0

        time = 0
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]
        while  queue:
            (ROW, COL), CURRENTTIME = queue.popleft()
            time = max(CURRENTTIME, time)
            for i in range(4):
                nrow = ROW + drow[i]
                ncol = COL + dcol[i]
                if (nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and grid[nrow][ncol] == 1 and vis[nrow][ncol] != 2):
                    queue.append(((nrow, ncol), CURRENTTIME + 1))
                    vis[nrow][ncol] = 2

        for row in range(n):
            for col in range(m):
                if (vis[row][col] != 2 and grid[row][col] == 1):
                    return -1
        return time


                

        