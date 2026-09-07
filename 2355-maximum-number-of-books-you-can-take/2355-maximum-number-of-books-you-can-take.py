class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)

        dp = [0] * n
        stack = []

        ans = 0
        for i in range(n):
            while stack and books[stack[-1]] - stack[-1] >= books[i] - i:
                stack.pop()

            j = stack[-1] if stack else -1
            length = min(i - j, books[i])
            segment_sum = ((2 * books[i] - length + 1) * length // 2)

            if j != -1:
                dp[i] = dp[j] + segment_sum
            else:
                dp[i] = segment_sum

            ans = max(ans, dp[i])
            stack.append(i)

        return ans