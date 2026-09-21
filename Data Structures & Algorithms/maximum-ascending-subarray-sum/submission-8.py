class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        tsum = csum =nums[0]
        for num in range(1,len(nums)):
            if nums[num]<=nums[num-1]:
                csum = nums[num]
            else:
                csum+=nums[num]
            tsum = max(tsum,csum)
        return tsum
        