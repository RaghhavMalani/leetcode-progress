class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(room):
            if room in visited:
                return

            visited.add(room)

            keys = rooms[room]
            for key in keys:
                dfs(key) 

        dfs(0)
        return len(visited) == len(rooms)