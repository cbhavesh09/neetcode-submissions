class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        tsum = maxsum = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]>=nums[i]:
                tsum = 0
            tsum +=nums[i]
            maxsum = max(tsum,maxsum)
        return maxsum
        