class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = sum(range(len(nums)+1))
        sum_nums = sum(nums)
        num_left = total_sum-sum_nums
        return num_left