class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            adj[prerequisite].append(course)

        state = [0] * numCourses
        order = []

        def dfs(course):
            # Currently in DFS path: cycle detected
            if state[course] == 1:
                return False

            # Already fully processed
            if state[course] == 2:
                return True

            state[course] = 1

            for next_course in adj[course]:
                if not dfs(next_course):
                    return False

            state[course] = 2
            order.append(course)
            return True

        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return []

        return order[::-1]