class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def atMost(k):
            left = 0
            odd = 0
            ans = 0

            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    odd += 1

                while odd > k:
                    if nums[left] % 2 == 1:
                        odd -= 1
                    left += 1

                ans += right - left + 1

            return ans

        return atMost(k) - atMost(k - 1)