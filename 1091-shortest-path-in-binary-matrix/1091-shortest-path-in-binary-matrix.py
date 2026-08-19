class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[float('inf')] * n for _ in range(n)]
        
        sr, sc = 0, 0
        dr, dc = n-1, n-1

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
            
        if n == 1:
            return 1

        dist[sr][sc] = 1

        q = deque()
        q.append((1, sr, sc))

        row_dir = [-1, -1, -1, 0, 0, 1, 1, 1]
        col_dir = [-1,  0,  1, -1, 1, -1, 0, 1]

        while q:

            dis, r, c = q.popleft()

            for i in range(8):

                newr = r + row_dir[i]
                newc = c + col_dir[i]

                if (0 <= newr < n and 0 <= newc < n and grid[newr][newc] == 0 and dis + 1 < dist[newr][newc] ):

                    dist[newr][newc] = dis + 1

                    if newr == dr and newc == dc:
                        return dis + 1

                    q.append((dis + 1, newr, newc))

        return -1