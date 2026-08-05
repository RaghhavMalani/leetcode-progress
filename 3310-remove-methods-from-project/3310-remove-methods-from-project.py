class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for method, invoked_method in invocations:
            graph[method].append(invoked_method)
        suspicious = [False] * n
        stack = [k]
        suspicious[k] = True

        while stack:
            method = stack.pop()

            for next_method in graph[method]:
                if not suspicious[next_method]:
                    suspicious[next_method] = True
                    stack.append(next_method)

        for method, invoked_method in invocations:
            if not suspicious[method] and suspicious[invoked_method]:
                return list(range(n))


        return [method for method in range(n) if not suspicious[method]]