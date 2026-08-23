class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hset = {}
        for i,n in enumerate(nums):
            ans = target-n
            if ans in hset:
                return [hset[ans],i]
            hset[n]= i
        
        