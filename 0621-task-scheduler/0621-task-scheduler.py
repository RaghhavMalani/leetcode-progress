class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        maxheap = [-count for count in freq.values()]
        heapq.heapify(maxheap)

        q = deque()

        time = 0

        while maxheap or q:
            time += 1

            if maxheap:
                count = heapq.heappop(maxheap)
                count += 1

                if count != 0:
                    q.append((count, time + n))

            if q and q[0][1] == time:
                count, readyTime = q.popleft()
                heapq.heappush(maxheap, count)

        return time