class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ans = 0

        for x in arr:
            if x > ans:
                ans += 1

        return ans