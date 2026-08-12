class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            adj[prerequisite].append(course)

        visited = [False] * numCourses
        path_visited = [False] * numCourses

        def dfs(course):
            visited[course] = True
            path_visited[course] = True

            for next_course in adj[course]:
                if not visited[next_course]:
                    if dfs(next_course):
                        return True

                elif path_visited[next_course]:
                    return True

            path_visited[course] = False
            return False

        for course in range(numCourses):
            if not visited[course]:
                if dfs(course):
                    return False

        return True