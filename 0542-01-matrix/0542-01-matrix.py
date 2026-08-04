class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        vis = [[0 for _ in range(m)] for _ in range(n)]
        dis = [[0 for _ in range(m)] for _ in range(n)]

        q = deque()

        for row in range(n):
            for col in range(m):
                if mat[row][col] == 0:
                    dis[row][col] = 0
                    q.append(((row,col),0))
                    vis[row][col] = 1
        
        while q:
            (ROW, COL),STEP = q.popleft()
            distance = [(-1,0),(1,0),(0,1),(0,-1)]
            for (drow, dcol) in distance:
                nrow = ROW + drow
                ncol = COL + dcol
                if (nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and (not vis[nrow][ncol]) and mat[nrow][ncol] == 1):
                    q.append(((nrow, ncol),STEP + 1))
                    dis[nrow][ncol] = STEP + 1
                    vis[nrow][ncol] = 1

        return dis
                
        