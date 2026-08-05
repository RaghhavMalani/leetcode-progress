class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        def dfs(node, current_color):
            color[node] = current_color

            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    if not dfs(neighbor, 1 - current_color):
                        return False

                elif color[neighbor] == color[node]:
                    return False

            return True

        for node in range(n):
            if color[node] == -1:
                if not dfs(node, 0):
                    return False

        return True