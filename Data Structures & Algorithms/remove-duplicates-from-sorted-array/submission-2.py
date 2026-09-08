class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = 0
        for num in range(1,len(nums)):
            if nums[prev]!=nums[num]:
                nums[prev+1] = nums[num]
                prev+=1
        return prev+1
        