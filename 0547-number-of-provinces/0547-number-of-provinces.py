class Solution:
    def dfs(self, node, adj_list, visit):
        visit[node] = True
        for neighbor in adj_list[node]:
            if not visit[neighbor]:
                self.dfs(neighbor, adj_list, visit)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        V = len(isConnected)
        adj_list = [[] for _ in range(V)]
        
        for i in range(V):
            for j in range(V):
                if isConnected[i][j] == 1 and i != j:
                    adj_list[i].append(j)
                    adj_list[j].append(i)
        
        visit = [0] * V
        count = 0
        for i in range(V):
            if not visit[i]:
                count += 1
                self.dfs(i, adj_list, visit)

        return count
        