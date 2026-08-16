from collections import deque
from typing import List

class Solution:

    def topoSort(self, V, adj):

        indegree = [0] * V

        for i in range(V):
            for neighbor in adj[i]:
                indegree[neighbor] += 1

        q = deque()

        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        topo = []

        while q:

            node = q.popleft()
            topo.append(node)

            for neighbor in adj[node]:

                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return topo


    def alienOrder(self, words: List[str]) -> str:
        chars = set()

        for word in words:
            for ch in word:
                chars.add(ch)

        chars = list(chars)

        charToIndex = {}

        for i in range(len(chars)):
            charToIndex[chars[i]] = i

        V = len(chars)

        adj = [set() for _ in range(V)]

        N = len(words)
        for i in range(N - 1):

            s1 = words[i]
            s2 = words[i + 1]

            length = min(len(s1), len(s2))

            if len(s1) > len(s2) and s1[:length] == s2[:length]:
                return ""

            for ptr in range(length):

                if s1[ptr] != s2[ptr]:

                    u = charToIndex[s1[ptr]]
                    v = charToIndex[s2[ptr]]

                    adj[u].add(v)
                    break

        topo = self.topoSort(V, adj)

        if len(topo) != V:
            return ""

        ans = ""

        for node in topo:
            ans += chars[node]

        return ans