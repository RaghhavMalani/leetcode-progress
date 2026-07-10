class Solution {
public:
    vector<int> pathExistenceQueries(
        int n,
        vector<int>& nums,
        int maxDiff,
        vector<vector<int>>& queries
    ) {
        vector<pair<int, int>> sortedNodes;

        for (int i = 0; i < n; i++) {
            sortedNodes.push_back({nums[i], i});
        }

        sort(sortedNodes.begin(), sortedNodes.end());

        vector<int> values(n);
        vector<int> position(n);

        for (int i = 0; i < n; i++) {
            values[i] = sortedNodes[i].first;
            position[sortedNodes[i].second] = i;
        }

        vector<int> farthest(n);

        int right = 0;

        for (int left = 0; left < n; left++) {
            right = max(right, left);

            while (
                right + 1 < n &&
                values[right + 1] - values[left] <= maxDiff
            ) {
                right++;
            }

            farthest[left] = right;
        }

        vector<int> component(n, 0);

        for (int i = 1; i < n; i++) {
            component[i] = component[i - 1];

            if (values[i] - values[i - 1] > maxDiff) {
                component[i]++;
            }
        }

        int LOG = 1;

        while ((1 << LOG) <= n) {
            LOG++;
        }

        vector<vector<int>> jump(LOG, vector<int>(n));

        for (int i = 0; i < n; i++) {
            jump[0][i] = farthest[i];
        }

        for (int k = 1; k < LOG; k++) {
            for (int i = 0; i < n; i++) {
                jump[k][i] = jump[k - 1][jump[k - 1][i]];
            }
        }

        vector<int> answer;

        for (const vector<int>& query : queries) {
            int left = position[query[0]];
            int right = position[query[1]];

            if (left > right) {
                swap(left, right);
            }

            if (left == right) {
                answer.push_back(0);
                continue;
            }

            if (component[left] != component[right]) {
                answer.push_back(-1);
                continue;
            }

            int current = left;
            int distance = 0;

            for (int k = LOG - 1; k >= 0; k--) {
                int nextPosition = jump[k][current];

                if (nextPosition > current && nextPosition < right) {
                    current = nextPosition;
                    distance += (1 << k);
                }
            }

            answer.push_back(distance + 1);
        }

        return answer;
    }
};