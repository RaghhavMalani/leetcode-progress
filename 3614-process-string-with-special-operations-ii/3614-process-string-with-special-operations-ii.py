class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        length = [0] * (n + 1)

        for i, ch in enumerate(s):
            curr = length[i]

            if ch.isalpha():
                curr += 1
            elif ch == '*':
                if curr > 0:
                    curr -= 1
            elif ch == '#':
                curr *= 2
            elif ch == '%':
                curr = curr

            length[i + 1] = curr

        if k >= length[n]:
            return '.'

        for i in range(n - 1, -1, -1):
            ch = s[i]
            before = length[i]
            after = length[i + 1]

            if ch.isalpha():
                if k == before:
                    return ch

            elif ch == '*':
                pass

            elif ch == '#':
                if before > 0:
                    k %= before

            elif ch == '%':
                k = before - 1 - k

        return '.'