class Solution:
    def minimumPushes(self, word: str) -> int:
        frequency = Counter(word)

        frequencies = sorted(frequency.values(), reverse=True)

        pushes = 0
        for i, freq in enumerate(frequencies):
            cost = (i // 8) + 1
            pushes += freq * cost

        return pushes