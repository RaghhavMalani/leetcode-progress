class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        freq = [0] * 100001

        for c in costs:
            freq[c] += 1

        ans = 0

        for price in range(1, 100001):
            if freq[price] > 0:
                buy = min(freq[price], coins // price)
                ans += buy
                coins -= buy * price

        return ans