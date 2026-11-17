class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hset = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in hset:
                return [hset[diff],index]
            hset[num]=index
        


        