class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = Counter(s)

        odd = [c for c in freq if freq[c] % 2]

        if len(odd) > 1:
            return ""

        if n % 2 == 0 and odd:
            return ""

        middle = odd[0] if odd else ""

        m = n // 2

        cnt = [0] * 26

        for c, f in freq.items():
            cnt[ord(c) - ord('a')] = f // 2

        t = target[:m]

        rem = [None] * (m + 1)
        rem[0] = cnt[:]

        matched = 0

        for i in range(m):
            cur = rem[i]

            if cur is None:
                break

            x = ord(t[i]) - ord('a')

            if cur[x] == 0:
                break

            nxt = cur[:]
            nxt[x] -= 1

            rem[i + 1] = nxt
            matched = i + 1

        if rem[m] is not None:
            left = t
            palindrome = left + middle + left[::-1]

            if palindrome > target:
                return palindrome

        for i in range(min(m - 1, matched), -1, -1):

            if rem[i] is None:
                continue

            counts = rem[i][:]
            target_char = ord(t[i]) - ord('a')

            bigger = -1

            for c in range(target_char + 1, 26):
                if counts[c] > 0:
                    bigger = c
                    break

            if bigger == -1:
                continue

            counts[bigger] -= 1

            left = list(t[:i])
            left.append(chr(bigger + ord('a')))

            for c in range(26):
                left.extend([chr(c + ord('a'))] * counts[c])

            left = ''.join(left)

            return left + middle + left[::-1]

        return ""