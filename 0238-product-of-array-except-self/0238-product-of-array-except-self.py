class Solution(object):

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]
        
        postfix = 1 
        for j in range(len(nums)-1, -1, -1):
            res[j] = res[j] * postfix
            postfix = nums[j] * postfix

        return res