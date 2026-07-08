class Solution {
    public int minimumEffortPath(int[][] heights) {
        int ROWS = heights.length;
        int COLS = heights[0].length;

        // minHeap stores {diff, row, col}
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(
            (a, b) -> a[0] - b[0]
        );

        minHeap.offer(new int[]{0, 0, 0});

        boolean[][] visited = new boolean[ROWS][COLS];

        int[][] directions = {
            {1, 0},
            {0, 1},
            {0, -1},
            {-1, 0}
        };

        while (!minHeap.isEmpty()) {
            int[] curr = minHeap.poll();

            int diff = curr[0];
            int r = curr[1];
            int c = curr[2];

            if (visited[r][c]) {
                continue;
            }

            visited[r][c] = true;

            if (r == ROWS - 1 && c == COLS - 1) {
                return diff;
            }

            for (int[] dir : directions) {
                int newR = r + dir[0];
                int newC = c + dir[1];

                if (
                    newR < 0 || newC < 0 ||
                    newR == ROWS || newC == COLS ||
                    visited[newR][newC]
                ) {
                    continue;
                }

                int newDiff = Math.max(
                    diff,
                    Math.abs(heights[r][c] - heights[newR][newC])
                );

                minHeap.offer(new int[]{newDiff, newR, newC});
            }
        }

        return 0;
    }
}