class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int ROWS = heights.size();
        int COLS = heights[0].size();

        // minHeap stores {diff, row, col}
        priority_queue<
            vector<int>,
            vector<vector<int>>,
            greater<vector<int>>
        > minHeap;

        minHeap.push({0, 0, 0});

        vector<vector<bool>> visited(ROWS, vector<bool>(COLS, false));

        vector<vector<int>> directions = {
            {1, 0},
            {0, 1},
            {0, -1},
            {-1, 0}
        };

        while (!minHeap.empty()) {
            vector<int> curr = minHeap.top();
            minHeap.pop();

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

            for (auto& dir : directions) {
                int newR = r + dir[0];
                int newC = c + dir[1];

                if (
                    newR < 0 || newC < 0 ||
                    newR == ROWS || newC == COLS ||
                    visited[newR][newC]
                ) {
                    continue;
                }

                int newDiff = max(
                    diff,
                    abs(heights[r][c] - heights[newR][newC])
                );

                minHeap.push({newDiff, newR, newC});
            }
        }

        return 0;
    }
};