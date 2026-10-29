class Solution:
    def palindromePath(
        self,
        n: int,
        edges: list[list[int]],
        s: str,
        queries: list[str]
    ) -> list[bool]:

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = max(1, n.bit_length())

        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        children = [[] for _ in range(n)]

        # ---------------------------------
        # 1. Root tree at node 0
        # ---------------------------------
        order = [0]
        parent[0][0] = 0

        for u in order:
            for v in graph[u]:
                if v == parent[0][u] and u != 0:
                    continue

                if v == 0:
                    continue

                parent[0][v] = u
                depth[v] = depth[u] + 1
                children[u].append(v)
                order.append(v)

        # Binary lifting table
        for j in range(1, LOG):
            for u in range(n):
                parent[j][u] = parent[j - 1][parent[j - 1][u]]

        # ---------------------------------
        # 2. Euler tour
        # ---------------------------------
        tin = [0] * n
        tout = [0] * n
        euler = [0] * n

        timer = 0
        stack = [(0, 0)]   # node, state

        while stack:
            u, state = stack.pop()

            if state == 0:
                tin[u] = timer
                euler[timer] = u
                timer += 1

                stack.append((u, 1))

                for v in reversed(children[u]):
                    stack.append((v, 0))

            else:
                tout[u] = timer - 1

        # ---------------------------------
        # 3. Initial root -> node XOR masks
        # ---------------------------------
        chars = list(s)
        prefix = [0] * n

        prefix[0] = 1 << (ord(chars[0]) - ord('a'))

        for u in order[1:]:
            p = parent[0][u]

            prefix[u] = (
                prefix[p]
                ^ (1 << (ord(chars[u]) - ord('a')))
            )

        # Convert prefix values into Euler order
        values = [0] * n

        for i in range(n):
            values[i] = prefix[euler[i]]

        # ---------------------------------
        # Fenwick tree:
        # range XOR update + point query
        # ---------------------------------
        bit = [0] * (n + 2)

        def add(i, val):
            i += 1

            while i <= n + 1:
                bit[i] ^= val
                i += i & -i

        def query(i):
            i += 1
            ans = 0

            while i > 0:
                ans ^= bit[i]
                i -= i & -i

            return ans

        # Store XOR difference array
        previous = 0

        for i in range(n):
            diff = values[i] ^ previous
            add(i, diff)
            previous = values[i]

        def range_xor(left, right, val):
            add(left, val)

            if right + 1 < n:
                add(right + 1, val)

        # ---------------------------------
        # LCA
        # ---------------------------------
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for j in range(LOG):
                if diff & (1 << j):
                    u = parent[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if parent[j][u] != parent[j][v]:
                    u = parent[j][u]
                    v = parent[j][v]

            return parent[0][u]

        # ---------------------------------
        # Process queries
        # ---------------------------------
        answer = []

        for command in queries:
            parts = command.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_char = parts[2]

                old_bit = 1 << (ord(chars[u]) - ord('a'))
                new_bit = 1 << (ord(new_char) - ord('a'))

                delta = old_bit ^ new_bit

                if delta:
                    # Every root->descendant path contains u,
                    # so all prefix masks in u's subtree change.
                    range_xor(tin[u], tout[u], delta)
                    chars[u] = new_char

            else:
                u = int(parts[1])
                v = int(parts[2])

                w = lca(u, v)

                prefix_u = query(tin[u])
                prefix_v = query(tin[v])

                lca_bit = 1 << (ord(chars[w]) - ord('a'))

                path_mask = prefix_u ^ prefix_v ^ lca_bit

                # At most one odd-frequency character
                answer.append(
                    path_mask == 0
                    or (path_mask & (path_mask - 1)) == 0
                )

        return answer