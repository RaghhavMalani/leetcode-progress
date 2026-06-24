class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        d = 2 * m

        def mat_mul(A, B):
            C = [[0] * d for _ in range(d)]
            for i in range(d):
                Ci = C[i]
                Ai = A[i]
                for k in range(d):
                    if Ai[k]:
                        a = Ai[k]
                        Bk = B[k]
                        for j in range(d):
                            Ci[j] += a * Bk[j]
                for j in range(d):
                    Ci[j] %= MOD
            return C

        def mat_vec_mul(A, v):
            res = [0] * d
            for i in range(d):
                total = 0
                Ai = A[i]
                for j in range(d):
                    total += Ai[j] * v[j]
                res[i] = total % MOD
            return res

        state = [0] * d

        for x in range(1, m + 1):
            state[x - 1] = x - 1
            state[m + x - 1] = m - x

        T = [[0] * d for _ in range(d)]

        for x in range(1, m + 1):
            for y in range(1, x):
                T[x - 1][m + y - 1] = 1

            for y in range(x + 1, m + 1):
                T[m + x - 1][y - 1] = 1

        power = n - 2

        while power:
            if power & 1:
                state = mat_vec_mul(T, state)

            T = mat_mul(T, T)
            power >>= 1

        return sum(state) % MOD