class Solution:
    def countServers(
        self,
        n: int,
        logs: list[list[int]],
        x: int,
        queries: list[int]
    ) -> list[int]:

        logs.sort(key=lambda log: log[1])

        sorted_queries = sorted(
            (time, i)
            for i, time in enumerate(queries)
        )

        count = [0] * (n + 1)
        active = 0

        left = 0
        right = 0

        ans = [0] * len(queries)

        for q, index in sorted_queries:

            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]

                if count[server] == 0:
                    active += 1

                count[server] += 1
                right += 1

            while left < right and logs[left][1] < q - x:
                server = logs[left][0]

                count[server] -= 1

                if count[server] == 0:
                    active -= 1

                left += 1

            ans[index] = n - active

        return ans