class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]

        for u, v, price in flights:
            adj[u].append((v, price))

        dist = [float('inf')] * n
        dist[src] = 0

        # (stops, node, cost)
        q = deque()
        q.append((0, src, 0))

        while q:

            stops, node, cost = q.popleft()

            # Cannot take another flight
            if stops > k:
                continue

            for neighbor, price in adj[node]:

                newCost = cost + price

                if newCost < dist[neighbor]:

                    dist[neighbor] = newCost

                    q.append(
                        (stops + 1, neighbor, newCost)
                    )

        if dist[dst] == float('inf'):
            return -1

        return dist[dst]
        