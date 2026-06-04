class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        nums_s = set(nums)

        for val in nums_s:
            hashmap[val] = nums.count(val)

        sorted_items = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        res = []

        for num, freq in sorted_items:
            if k > 0:
                res.append(num)
                k -= 1
            else:
                break

        return res