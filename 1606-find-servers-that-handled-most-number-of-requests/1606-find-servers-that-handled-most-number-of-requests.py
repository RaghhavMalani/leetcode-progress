class Solution:
    def busiestServers(
        self,
        k: int,
        arrival: list[int],
        load: list[int]
    ) -> list[int]:

        bit = [0] * (k + 1)

        def add(i, delta):
            i += 1

            while i <= k:
                bit[i] += delta
                i += i & -i

        def prefix(i):
            if i < 0:
                return 0

            i += 1
            total = 0

            while i > 0:
                total += bit[i]
                i -= i & -i

            return total

        def kth(order):
            idx = 0
            step = 1 << (k.bit_length() - 1)

            while step:
                nxt = idx + step

                if nxt <= k and bit[nxt] < order:
                    idx = nxt
                    order -= bit[nxt]

                step >>= 1

            return idx

        for server in range(k):
            add(server, 1)

        busy = []
        handled = [0] * k

        for i, (time, duration) in enumerate(zip(arrival, load)):

            while busy and busy[0][0] <= time:
                _, server = heapq.heappop(busy)
                add(server, 1)

            available = prefix(k - 1)

            if available == 0:
                continue

            start = i % k
            before = prefix(start - 1)

            if available - before > 0:
                server = kth(before + 1)
            else:
                server = kth(1)

            add(server, -1)
            handled[server] += 1

            heapq.heappush(
                busy,
                (time + duration, server)
            )

        maximum = max(handled)

        return [
            i
            for i in range(k)
            if handled[i] == maximum
        ]