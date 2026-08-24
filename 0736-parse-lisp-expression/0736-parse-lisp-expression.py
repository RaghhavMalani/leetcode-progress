class Solution:
    def evaluate(self, expression: str) -> int:
        
        def parse(expr, scope):

            if expr[0] == '-' or expr[0].isdigit():
                return int(expr)
            
            if expr[0] != '(':
                return scope[expr]

            inner = expr[1:-1]
            tokens = []
            balance = 0
            start = 0

            for i, ch in enumerate(inner):
                if ch == "(":
                    balance += 1

                elif ch == ')':
                    balance -= 1

                elif ch == ' ' and balance == 0:
                    tokens.append(inner[start:i])
                    start = i + 1

            tokens.append(inner[start:])
            operation = tokens[0]
            if operation == "add":
                return (
                    parse(tokens[1], scope) + parse(tokens[2], scope))

            if operation == "mult":
                return (parse(tokens[1], scope)* parse(tokens[2], scope) )

            newScope = scope.copy()
            i = 1

            while i < len(tokens) - 1:
                variable = tokens[i]
                value = parse(tokens[i + 1], newScope)
                newScope[variable] = value
                i += 2

            return parse(tokens[-1], newScope)

        return parse(expression, {})
