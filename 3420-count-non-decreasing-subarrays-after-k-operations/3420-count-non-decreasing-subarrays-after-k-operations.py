class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dq = deque()
        cost = 0
        right = n - 1
        ans = 0

        for left in range(n - 1, -1, -1):
            x = nums[left]
            count = 1

            while dq and dq[0][0] < x:
                value, freq = dq.popleft()
                cost += (x - value) * freq
                count += freq

            if dq and dq[0][0] == x:
                _, freq = dq.popleft()
                count += freq

            dq.appendleft([x, count])

            while cost > k:
                value, freq = dq[-1]
                cost -= value - nums[right]

                if freq == 1:
                    dq.pop()
                else:
                    dq[-1][1] -= 1

                right -= 1

            ans += right - left + 1

        return ans