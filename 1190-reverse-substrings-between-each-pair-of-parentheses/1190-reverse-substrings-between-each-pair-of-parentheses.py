class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        current = ""

        for ch in s:
            if ch == '(':
                stack.append(current)
                current = ""

            elif ch == ')':
                current = current[::-1]
                current = stack.pop() + current

            else:
                current += ch

        return current
    