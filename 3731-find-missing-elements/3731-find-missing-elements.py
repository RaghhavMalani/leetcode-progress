class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        present = set(nums)

        smallest = min(nums)
        largest = max(nums)

        missing = []

        for number in range(smallest, largest + 1):
            if number not in present:
                missing.append(number)

        return missing