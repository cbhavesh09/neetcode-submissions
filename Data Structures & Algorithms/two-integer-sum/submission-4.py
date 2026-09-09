class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hset = {}
        for num in range(len(nums)):
            tofind = target-nums[num]
            if tofind in hset:
                return [hset[tofind],num]
            hset[nums[num]] = num

        