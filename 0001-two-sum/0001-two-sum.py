class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hash = {}

        for i in range(len(nums)):
            rem = target - nums[i]

            if rem in hash:
                return [i,hash[rem]]
            
            hash[nums[i]] = i

        return []