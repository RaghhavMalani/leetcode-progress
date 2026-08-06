class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(node: int) -> None:
            visited[node] = True

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        components = 0

        for node in range(n):
            if not visited[node]:
                components += 1
                dfs(node)

        return components