class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n, m = len(s1), len(s2)

        best_start = -1
        best_len = float('inf')

        i = 0

        while i < n:
            j = 0

            # Forward
            while i < n:
                if s1[i] == s2[j]:
                    j += 1

                    if j == m:
                        break

                i += 1

            if i == n:
                break

            end = i

            # Backward
            j = m - 1

            while j >= 0:
                if s1[i] == s2[j]:
                    j -= 1
                i -= 1

            start = i + 1

            window_len = end - start + 1

            if window_len < best_len:
                best_len = window_len
                best_start = start

            # Try finding another window
            i = start + 1

        if best_start == -1:
            return ""

        return s1[best_start:best_start + best_len]