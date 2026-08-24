class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        # Build graph
        for u, v in pairs:
            adj[u].append(v)
            outdegree[u] += 1
            indegree[v] += 1

        # Default start
        start = pairs[0][0]

        # For an Eulerian path,
        # start node has outdegree = indegree + 1
        for node in outdegree:
            if outdegree[node] == indegree[node] + 1:
                start = node
                break

        path = []

        def dfs(node):

            while adj[node]:

                neighbor = adj[node].pop()

                dfs(neighbor)

            path.append(node)

        dfs(start)

        path.reverse()

        ans = []

        for i in range(len(path) - 1):
            ans.append([path[i], path[i + 1]])

        return ans


            



