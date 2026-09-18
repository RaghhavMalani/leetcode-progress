class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            x = ord(ch) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i

        def getRight(L):
            ch = ord(s[L]) - ord('a')
            R = last[ch]

            i = L
            while i <= R:
                x = ord(s[i]) - ord('a')
                if first[x] < L:
                    return -1

                R = max(R, last[x])

                i += 1

            return R

        ans = []
        prev_end = -1

        for i in range(n):
            x = ord(s[i]) - ord('a')

            if first[x] != i:
                continue

            R = getRight(i)

            if R == -1:
                continue

            if i > prev_end:
                ans.append(s[i:R + 1])

            else:
                ans[-1] = s[i:R + 1]

            prev_end = R

        return ans