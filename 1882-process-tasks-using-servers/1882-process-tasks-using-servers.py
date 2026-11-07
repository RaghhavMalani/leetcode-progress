class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = []
        busy = []

        for i, weight in enumerate(servers):
            heapq.heappush(available, (weight, i))

        ans = []
        time = 0

        for i, task_time in enumerate(tasks):
            time = max(time, i)

            while busy and busy[0][0] <= time:
                free_time, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    free_time, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            weight, index = heapq.heappop(available)

            ans.append(index)

            heapq.heappush(
                busy,
                (time + task_time, weight, index)
            )

        return ans