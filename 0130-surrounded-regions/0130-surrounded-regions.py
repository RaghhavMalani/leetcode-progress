class Solution:
    def dfs(self, row, col, board, vis):
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        vis[row][col] = 1
        n = len(board)
        m = len(board[0])

        for (drow, dcol) in directions:
            nrow = row + drow
            ncol = col + dcol
            if (nrow >= 0 and ncol >= 0 and nrow < n and ncol < m and (not vis[nrow][ncol]) and board[nrow][ncol] == "O"):
                self.dfs(nrow, ncol, board, vis)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        vis = [[0 for _ in range(m)] for _ in range(n)]

        for col in range(m):
            if (not vis[0][col]) and board[0][col] == "O":
                self.dfs(0, col, board, vis)
            
            if (not vis[n - 1][col]) and board[n - 1][col] == "O":
                self.dfs(n - 1, col, board, vis)

        for row in range(n):
            if (not vis[row][0]) and board[row][0] == "O":
                self.dfs(row, 0, board, vis)
            
            if (not vis[row][m - 1]) and board[row][m - 1] == "O":
                self.dfs(row, m - 1, board, vis)

        for row in range(n):
            for col in range(m):
                if (not vis[row][col] and board[row][col] == "O"):
                    board[row][col] = "X"
        
        