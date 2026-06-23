class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        up = [0] * (m + 2)
        down = [0] * (m + 2)

        for x in range(1, m + 1):
            up[x] = x - 1
            down[x] = m - x

        for _ in range(3, n + 1):
            new_up = [0] * (m + 2)
            new_down = [0] * (m + 2)

            prefix = 0
            for x in range(1, m + 1):
                new_up[x] = prefix
                prefix = (prefix + down[x]) % MOD

            suffix = 0
            for x in range(m, 0, -1):
                new_down[x] = suffix
                suffix = (suffix + up[x]) % MOD

            up, down = new_up, new_down

        return (sum(up) + sum(down)) % MOD