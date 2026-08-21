class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7

        adj = [[] for _ in range(n)]
        for u, v, time in roads:
            adj[u].append((v, time))
            adj[v].append((u, time))

        dist = [float('inf')] * n
        ways = [0] * n

        dist[0] = 0
        ways[0] = 1

        pq = [(0, 0)]

        while pq:
            dis, node = heapq.heappop(pq)

            if dis > dist[node]:
                continue

            for neighbor, time in adj[node]:
                newDist = dis + time

                if newDist < dist[neighbor]:
                    dist[neighbor] = newDist
                    ways[neighbor] = ways[node]
                    heapq.heappush(pq,(newDist, neighbor))

                elif newDist == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[n - 1]