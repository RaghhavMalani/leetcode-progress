class Fenwick:
    def __init__(self, size):
        self.bit = [0] * (size + 1)

    def add(self, idx, val):
        while idx < len(self.bit):
            self.bit[idx] += val
            idx += idx & -idx

    def query(self, idx):
        total = 0
        while idx > 0:
            total += self.bit[idx]
            idx -= idx & -idx
        return total


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        offset = n + 2
        size = 2 * n + 5

        fenwick = Fenwick(size)

        prefix = 0
        ans = 0

        fenwick.add(prefix + offset, 1)

        for x in nums:
            if x == target:
                prefix += 1
            else:
                prefix -= 1

            idx = prefix + offset

            ans += fenwick.query(idx - 1)

            fenwick.add(idx, 1)

        return ans