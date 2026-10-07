class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        def valid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = {s}

        while queue:
            ans = []

            for string in queue:
                if valid(string):
                    ans.append(string)

            # First valid level = minimum removals
            if ans:
                return ans

            next_level = set()

            for string in queue:
                for i in range(len(string)):

                    if string[i] not in '()':
                        continue

                    new_string = string[:i] + string[i + 1:]
                    next_level.add(new_string)

            queue = next_level