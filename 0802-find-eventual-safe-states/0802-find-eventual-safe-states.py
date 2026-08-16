class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        reverse_graph = [[] for _ in range(n)]
        outdegree = [0] * n

        for node in range(n):
            outdegree[node] = len(graph[node])

            for neighbor in graph[node]:
                reverse_graph[neighbor].append(node)

        queue = deque()

        for node in range(n):
            if outdegree[node] == 0:
                queue.append(node)

        is_safe = [False] * n

        while queue:
            node = queue.popleft()
            is_safe[node] = True

            for previous in reverse_graph[node]:
                outdegree[previous] -= 1

                if outdegree[previous] == 0:
                    queue.append(previous)

        return [node for node in range(n) if is_safe[node]]