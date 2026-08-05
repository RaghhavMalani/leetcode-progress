class Solution:
    def dfsCheck(self, node, graph, vis, pathVis, check):
        vis[node] = 1
        pathVis[node] = 1
        check[node] = 0

        for nbr in graph[node]:
            if (not vis[nbr]):
                if self.dfsCheck(nbr, graph, vis, pathVis, check):
                    check[node] = 0
                    return True
                
            elif pathVis[nbr]:
                check[node] = 0
                return True

        check[node] = 1
        pathVis[node] = 0
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        vis = [0] * n
        pathVis = [0] * n
        check = [0] * n
        safenodes = []
        for i in range(n):
            if not vis[i]:
                self.dfsCheck(i, graph, vis, pathVis, check)
            
        for i in range(n):
            if check[i] == 1:
                safenodes.append(i)
        
        return safenodes

                

        