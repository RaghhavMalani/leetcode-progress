class Solution:
    def findMaxPathScore(
        self,
        edges: List[List[int]],
        online: List[bool],
        k: int
    ) -> int:
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n

        max_cost = 0

        for u, v, cost in edges:
            graph[u].append((v, cost))
            indegree[v] += 1
            max_cost = max(max_cost, cost)

        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        topo = []

        while q:
            node = q.popleft()
            topo.append(node)

            for nei, cost in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        def can(min_edge_score: int) -> bool:
            INF = 10**30
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                if dist[u] > k:
                    continue

                if not online[u]:
                    continue

                for v, cost in graph[u]:
                    if cost < min_edge_score:
                        continue

                    if not online[v]:
                        continue

                    new_cost = dist[u] + cost

                    if new_cost < dist[v]:
                        dist[v] = new_cost

            return dist[n - 1] <= k

        ans = -1
        left = 0
        right = max_cost

        while left <= right:
            mid = (left + right) // 2

            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans