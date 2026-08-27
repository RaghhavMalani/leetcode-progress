class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum = sum(cardPoints[:k])
        right_sum = 0

        ans = left_sum

        for i in range(1, k + 1):
            left_sum -= cardPoints[k - i]
            right_sum += cardPoints[-i]

            ans = max(ans, left_sum + right_sum)

        return ans