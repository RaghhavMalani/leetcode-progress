class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s = list(s)

        prefix = [0] * (4 * n)
        suffix = [0] * (4 * n)
        best = [0] * (4 * n)
        length = [0] * (4 * n)

        def merge(node, leftNode, rightNode, l, mid, r):
            length[node] = length[leftNode] + length[rightNode]

            prefix[node] = prefix[leftNode]
            suffix[node] = suffix[rightNode]

            best[node] = max(
                best[leftNode],
                best[rightNode]
            )

            if s[mid] == s[mid + 1]:

                best[node] = max(
                    best[node],
                    suffix[leftNode] + prefix[rightNode]
                )

                if prefix[leftNode] == length[leftNode]:
                    prefix[node] = (
                        length[leftNode] + prefix[rightNode]
                    )

                if suffix[rightNode] == length[rightNode]:
                    suffix[node] = (
                        length[rightNode] + suffix[leftNode]
                    )

        def build(node, l, r):
            if l == r:
                prefix[node] = 1
                suffix[node] = 1
                best[node] = 1
                length[node] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            merge(
                node,
                node * 2,
                node * 2 + 1,
                l,
                mid,
                r
            )

        def update(node, l, r, index):
            if l == r:
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index)
            else:
                update(node * 2 + 1, mid + 1, r, index)

            merge(
                node,
                node * 2,
                node * 2 + 1,
                l,
                mid,
                r
            )

        build(1, 0, n - 1)

        answer = []

        for index, char in zip(queryIndices, queryCharacters):
            s[index] = char

            update(1, 0, n - 1, index)

            answer.append(best[1])

        return answer