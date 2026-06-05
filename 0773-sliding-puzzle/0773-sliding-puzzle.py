class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = "123450"

        start = ""
        for row in board:
            for num in row:
                start += str(num)

        if start == target:
            return 0

        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        q = deque()
        visited = set()

        zero_index = start.index("0")

        q.append((start, zero_index, 0))
        visited.add(start)

        while q:
            state, zero_index, moves = q.popleft()

            for next_index in neighbors[zero_index]:
                state_list = list(state)

                state_list[zero_index], state_list[next_index] = state_list[next_index], state_list[zero_index]

                new_state = "".join(state_list)

                if new_state == target:
                    return moves + 1

                if new_state not in visited:
                    visited.add(new_state)
                    q.append((new_state, next_index, moves + 1))

        return -1