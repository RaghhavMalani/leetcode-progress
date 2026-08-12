class Solution:
    def dfs(self, node, graph, vis, pathVis):
        vis[node] = 1
        pathVis[node] = 1

        for nbr in graph[node]:
            if not vis[nbr]:
                if self.dfs(nbr, graph, vis, pathVis):
                    return True

            elif pathVis[nbr]:
                return True

        pathVis[node] = 0
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            graph[pre].append(course)

        vis = [0] * numCourses
        pathVis = [0] * numCourses

        for node in range(numCourses):
            if not vis[node]:
                if self.dfs(node, graph, vis, pathVis):
                    return False

        return True