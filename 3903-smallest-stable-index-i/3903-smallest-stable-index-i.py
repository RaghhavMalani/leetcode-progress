class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        suffixMin = [0] * n
        suffixMin[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffixMin[i] = min(nums[i], suffixMin[i + 1])

        prefixMax = nums[0]

        for i in range(n):
            prefixMax = max(prefixMax, nums[i])

            if prefixMax - suffixMin[i] <= k:
                return i

        return -1