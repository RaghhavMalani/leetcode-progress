class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        count = 0

        while queue:
            node = queue.popleft()
            count += 1

            for nbr in graph[node]:
                indegree[nbr] -= 1

                if indegree[nbr] == 0:
                    queue.append(nbr)

        return count == numCourses

