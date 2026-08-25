class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) #7
        k %= n #k = k % 7 - 3% 7 = 3
        temp = [0] * n

        for i in range(n):

            newIndex = (i + k) % n # 
            temp[newIndex] = nums[i]

        nums[:] = temp
