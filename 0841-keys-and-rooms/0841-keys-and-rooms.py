class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        vis = [0] * n
        queue = deque()
        start = 0
        queue.append(start)

        while queue:
            current = queue.popleft()
            vis[current] = 1
            
            for nbr in rooms[current]:
                if vis[nbr] == 0:
                    vis[nbr] = 1
                    queue.append(nbr)
                else:
                    continue

        if 0 in vis:
            return False
        
        return True
