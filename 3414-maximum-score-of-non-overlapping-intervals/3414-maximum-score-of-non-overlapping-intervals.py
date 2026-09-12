class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        arr = sorted((l, r, w, i) for i, (l, r, w) in enumerate(intervals) )
        n = len(arr)
        starts = [arr[i][0] for i in range(n)]
        next_idx = [0] * n

        for i in range(n):
            r = arr[i][1]
            next_idx[i] = bisect_right(starts, r)

        dp = [ [(0, ()) for _ in range(5)]for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):

            l, r, weight, original_idx = arr[i]

            for k in range(1, 5):
                skip_score, skip_indices = dp[i + 1][k]

                j = next_idx[i]

                next_score, next_indices = dp[j][k - 1]
                take_score = weight + next_score
                take_indices = tuple(sorted(next_indices + (original_idx,)))

                if take_score > skip_score:
                    dp[i][k] = (take_score, take_indices)

                elif take_score == skip_score:
                    dp[i][k] = (take_score,min(take_indices, skip_indices) )

                else:
                    dp[i][k] = (skip_score, skip_indices)

        return list(dp[0][4][1])