class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for u, v, weight in edges:
            dist[u][v] = weight
            dist[v][u] = weight

        for via in range(n):
            for i in range(n):
                for j in range(n):

                    dist[i][j] = min(dist[i][j], dist[i][via] + dist[via][j] )

        minCities = float('inf')
        answer = -1

        for city in range(n):

            count = 0

            for neighbor in range(n):

                if (
                    city != neighbor
                    and dist[city][neighbor] <= distanceThreshold
                ):
                    count += 1

            if count <= minCities:
                minCities = count
                answer = city

        return answer