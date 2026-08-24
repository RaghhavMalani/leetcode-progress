class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))

        last = {}

        for i, digit in enumerate(digits):
            last[int(digit)] = i

        for i in range(len(digits)):
            current = int(digits[i])
            for digit in range(9, current, -1):
                if digit in last and last[digit] > i:
                    j = last[digit]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))

        return num

        