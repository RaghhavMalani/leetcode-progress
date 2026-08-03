class Solution:
    def dfs(self, sr, sc, image, vis, color, scolor):
        n = len(image)
        m = len(image[0])
        vis[sr][sc] = 1
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]
        image[sr][sc] = color
        for i in range(4):
            nrow = sr + drow[i]
            ncol = sc + dcol[i]
            if (nrow >= 0 and ncol >= 0 and nrow < n and ncol < m and (not vis[nrow][ncol]) and image[nrow][ncol] == scolor):
                vis[nrow][ncol] = 1
                self.dfs(nrow, ncol, image, vis, color, scolor)
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        scolor = image[sr][sc]
        vis = [[0 for _ in range(m)] for _ in range(n)]
        self.dfs(sr, sc, image, vis, color, scolor)
        return image

        
        