class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])

        restrictions.sort()

        m = len(restrictions)

        for i in range(1, m):
            prev_id, prev_height = restrictions[i - 1]
            curr_id, curr_height = restrictions[i]

            distance = curr_id - prev_id
            restrictions[i][1] = min(curr_height, prev_height + distance)

        for i in range(m - 2, -1, -1):
            curr_id, curr_height = restrictions[i]
            next_id, next_height = restrictions[i + 1]

            distance = next_id - curr_id
            restrictions[i][1] = min(curr_height, next_height + distance)

        ans = 0

        for i in range(1, m):
            left_id, left_height = restrictions[i - 1]
            right_id, right_height = restrictions[i]

            distance = right_id - left_id

            peak = (left_height + right_height + distance) // 2
            ans = max(ans, peak)

        return ans