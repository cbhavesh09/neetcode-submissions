class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        l = 0
        for num in range(1,len(nums)):
            if nums[l]==nums[num]:
                return True
            l+=1
        return False
        