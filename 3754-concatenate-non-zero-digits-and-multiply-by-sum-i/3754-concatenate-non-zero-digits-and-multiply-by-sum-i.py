class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)

        x_str = ""
        digit_sum = 0

        for ch in s:
            if ch != '0':
                x_str += ch
                digit_sum += int(ch)

        if x_str == "":
            return 0

        x = int(x_str)
        return x * digit_sum