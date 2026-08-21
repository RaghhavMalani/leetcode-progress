class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]

        for u, v, time in times:
            adj[u].append((v, time))

        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        minheap = [(0, k)]

        while minheap:
            dis, node = heapq.heappop(minheap)
            if dis > dist[node]:
                continue
            
            for neighbor, time in adj[node]:
                newDist = dis + time

                if newDist < dist[neighbor]:
                    dist[neighbor] = newDist
                    heapq.heappush(minheap, (newDist, neighbor))

        ans = max(dist[1:])

        if ans == float('inf'):
            return -1
        
        return ans
        