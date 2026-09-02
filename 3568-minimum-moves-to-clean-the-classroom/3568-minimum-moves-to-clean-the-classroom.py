class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        litter = [[-1] * n for _ in range(m)]
        k = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c

                elif classroom[r][c] == 'L':
                    litter[r][c] = k
                    k += 1

        if k == 0:
            return 0

        full_mask = (1 << k) - 1

        best = [ [[-1] * (1 << k) for _ in range(n)] for _ in range(m) ]

        best[sr][sc][0] = energy

        q = deque([ (sr, sc, 0, energy, 0) ])

        directions = ( (1, 0), (-1, 0), (0, 1), (0, -1) )

        while q:
            r, c, mask, curr_energy, moves = q.popleft()

            if curr_energy < best[r][c][mask]:
                continue

            if mask == full_mask:
                return moves

            if curr_energy == 0:
                continue

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if ( nr < 0 or nr >= m or nc < 0 or nc >= n or classroom[nr][nc] == 'X'):
                    continue

                new_energy = curr_energy - 1
                new_mask = mask

                if classroom[nr][nc] == 'L':
                    bit = litter[nr][nc]
                    new_mask |= 1 << bit

                if classroom[nr][nc] == 'R':
                    new_energy = energy

                if new_mask == full_mask:
                    return moves + 1

                if new_energy <= best[nr][nc][new_mask]:
                    continue

                best[nr][nc][new_mask] = new_energy

                q.append(( nr,nc,new_mask,new_energy, moves + 1 ))

        return -1