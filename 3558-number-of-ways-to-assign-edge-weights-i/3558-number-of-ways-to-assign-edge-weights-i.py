class Solution(object):
    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(edges) + 1
        
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        depth = 0
        visited = [False] * (n + 1)
        visited[1] = True
        queue = deque([1])
        
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for nxt in adj[node]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        queue.append(nxt)

        d = depth - 1  
        return pow(2, d - 1, MOD)