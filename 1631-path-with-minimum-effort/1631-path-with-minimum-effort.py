class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS = len(heights)
        COLS = len(heights[0])

        difference = [[float('inf')] * COLS for _ in range(ROWS)]
        
        sr, sc = 0, 0
        dr, dc = ROWS - 1, COLS - 1

        difference[sr][sc] = 0
        minheap = [[0, 0, 0]]
        
        row_dir = [-1, 0, 1, 0]
        col_dir = [0, 1, 0, -1]

        while minheap:
            dis, r, c = heapq.heappop(minheap)

            if r == dr and c == dc:
                return dis

            for i in range(4):
                newr = r + row_dir[i]
                newc = c + col_dir[i]

                if (newr >= 0 and newr < ROWS and newc >= 0 and newc < COLS):
                    newdiff = abs(heights[r][c] - heights[newr][newc])
                    MAX = max(newdiff, dis)

                    if difference[newr][newc] > MAX:
                        difference[newr][newc] = MAX
                        heapq.heappush(minheap, [MAX, newr, newc])

