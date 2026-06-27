class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 1

        if 1 in freq:
            ones = freq[1]
            if ones % 2 == 1:
                ans = max(ans, ones)
            else:
                ans = max(ans, ones - 1)

        for x in freq:
            if x == 1:
                continue

            length = 1
            cur = x
            while freq[cur] >= 2 and cur * cur in freq:
                length += 2
                cur = cur * cur

            ans = max(ans, length)

        return ans