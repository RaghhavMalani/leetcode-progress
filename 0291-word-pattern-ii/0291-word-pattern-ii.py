class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        mapping = {}
        used = set()

        def dfs(i, j):
            if i == len(pattern) and j == len(s):
                return True

            if i == len(pattern) or j == len(s):
                return False

            ch = pattern[i]

            if ch in mapping:
                word = mapping[ch]

                if not s.startswith(word, j):
                    return False

                return dfs(i + 1, j + len(word))

            for end in range(j + 1, len(s) + 1):
                candidate = s[j:end]

                if candidate in used:
                    continue

                mapping[ch] = candidate
                used.add(candidate)

                if dfs(i + 1, end):
                    return True

                del mapping[ch]
                used.remove(candidate)

            return False

        return dfs(0, 0)