class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in range(len(nums))]
        prefix = 1
        for num in range(len(nums)):
            res[num]=prefix
            prefix *=nums[num]
        postfix = 1
        for n in range(len(nums)-1,-1,-1):
            res[n]*=postfix
            postfix*= nums[n]
        return res

        