class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        left = 0 
        product = 1
        ans = 0

        for right in range(len(nums)):
            product =  product * nums[right]

            while product >= k :
                product = product // nums[left]
                left = left + 1

            ans = ans + (right - left) + 1

        return ans