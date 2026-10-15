class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        nines = sum // 9
        rem = sum % 9

        ans = "9" * nines

        if rem > 0:
            ans += str(rem)

        zeros = num - nines - (1 if rem > 0 else 0)
        ans += "0" * zeros

        return ans