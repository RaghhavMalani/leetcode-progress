class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k == n:
            return max(nums)

        freq = Counter(nums)

        if k == 1:
            ans = -1

            for num in nums:
                if freq[num] == 1:
                    ans = max(ans, num)

            return ans

        ans = -1

        if freq[nums[0]] == 1:
            ans = max(ans, nums[0])

        if freq[nums[-1]] == 1:
            ans = max(ans, nums[-1])

        return ans       