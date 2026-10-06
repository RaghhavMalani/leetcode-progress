class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        additions = 0

        for ch in s:
            if ch == '(':
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    additions += 1

        return additions + open_brackets