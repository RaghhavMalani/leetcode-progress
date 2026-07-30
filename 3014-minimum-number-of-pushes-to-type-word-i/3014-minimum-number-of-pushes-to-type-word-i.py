class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)

        one_push = min(n, 8)
        two_push = min(max(n - 8, 0), 8)
        three_push = min(max(n - 16, 0), 8)
        four_push = max(n - 24, 0)

        return (
            one_push
            + two_push * 2
            + three_push * 3
            + four_push * 4
        )