class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k >len(nums):
            return None
        nums.sort()
        l,r = 0,k-1
        fdiff = float('inf')
        while r<len(nums):
            minv = min(nums[l:r+1])
            maxv= max(nums[l:r+1])
            diff = maxv-minv
            fdiff = min(diff,fdiff)
            l+=1
            r+=1
        return fdiff



        