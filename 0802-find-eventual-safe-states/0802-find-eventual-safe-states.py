from typing import List

class Solution:
    def dfsCheck(self, node, graph, vis, pathVis, check):
        vis[node] = 1
        pathVis[node] = 1

        for nbr in graph[node]:
            if not vis[nbr]:
                if self.dfsCheck(nbr, graph, vis, pathVis, check):
                    return True

            elif pathVis[nbr]:
                return True

        check[node] = 1
        pathVis[node] = 0
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        vis = [0] * n
        pathVis = [0] * n
        check = [0] * n

        for node in range(n):
            if not vis[node]:
                self.dfsCheck(node, graph, vis, pathVis, check)

        safeNodes = []

        for node in range(n):
            if check[node] == 1:
                safeNodes.append(node)

        return safeNodes