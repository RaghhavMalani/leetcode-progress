class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        left_sum = 0
        answer = []

        for num in nums:
            right_sum = total_sum - left_sum - num

            difference = abs(left_sum - right_sum)
            answer.append(difference)

            left_sum += num

        return answer