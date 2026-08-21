class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()

        filtered = []
        for coin in coins:
            if not any(coin % x == 0 for x in filtered):
                filtered.append(coin)

        coins = filtered
        n = len(coins)

        terms = []

        def generate(index, current_lcm, size):
            for i in range(index, n):
                new_lcm = current_lcm // gcd(current_lcm, coins[i]) * coins[i]

                if size % 2 == 0:
                    terms.append((new_lcm, 1))
                else:
                    terms.append((new_lcm, -1))

                generate(i + 1, new_lcm, size + 1)

        generate(0, 1, 0)

        def count(x):
            total = 0

            for lcm, sign in terms:
                total += sign * (x // lcm)

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = left + (right - left) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left