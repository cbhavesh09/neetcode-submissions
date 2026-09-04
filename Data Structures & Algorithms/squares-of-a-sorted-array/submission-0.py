class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for num in range(len(nums)):
            nums[num] *=nums[num]
        for i in range(len(nums)):
            for j in range(0,len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]= nums[j+1],nums[j]
        return nums
        