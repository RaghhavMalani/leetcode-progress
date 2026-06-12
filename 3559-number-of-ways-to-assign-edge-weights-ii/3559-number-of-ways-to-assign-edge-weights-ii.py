class Solution:
    MOD = 10**9 + 7

    def assignEdgeWeights(
        self,
        edges: List[List[int]],
        queries: List[List[int]]
    ) -> List[int]:

        n = len(edges) + 1
        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = n.bit_length()

        depth = [0] * (n + 1)

        up = [[0] * (n + 1) for _ in range(LOG)]

        stack = [(1, 1)]

        while stack:
            node, parent = stack.pop()

            up[0][node] = parent

            for j in range(1, LOG):
                previous_ancestor = up[j - 1][node]
                up[j][node] = up[j - 1][previous_ancestor]

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue

                depth[neighbor] = depth[node] + 1
                stack.append((neighbor, node))

        def lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u

            depth_difference = depth[u] - depth[v]
            for j in range(LOG):
                if depth_difference & (1 << j):
                    u = up[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return up[0][u]

        powers_of_two = [1] * (n + 1)

        for i in range(1, n + 1):
            powers_of_two[i] = (
                powers_of_two[i - 1] * 2
            ) % self.MOD

        answer = []

        for u, v in queries:
            ancestor = lca(u, v)

            path_length = (
                depth[u]
                + depth[v]
                - 2 * depth[ancestor]
            )

            if path_length == 0:
                answer.append(0)
            else:
                answer.append(
                    powers_of_two[path_length - 1]
                )

        return answer