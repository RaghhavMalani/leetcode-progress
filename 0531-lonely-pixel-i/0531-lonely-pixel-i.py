class Solution:
    def findLonelyPixel(self, picture: list[list[str]]) -> int:
        m = len(picture)
        n = len(picture[0])

        row_count = [0] * m
        col_count = [0] * n

        for r in range(m):
            for c in range(n):
                if picture[r][c] == 'B':
                    row_count[r] += 1
                    col_count[c] += 1

        ans = 0

        for r in range(m):
            for c in range(n):
                if (
                    picture[r][c] == 'B'
                    and row_count[r] == 1
                    and col_count[c] == 1
                ):
                    ans += 1

        return ans