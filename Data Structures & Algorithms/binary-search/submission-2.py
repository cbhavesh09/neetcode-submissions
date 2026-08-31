class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            m1 = l+(r-l)//3
            m2 = r-(r-l)//3
            if target == nums[m1]:
                return m1
            if target == nums[m2]:
                return m2
            elif target<nums[m1]:
                r=m1-1
            elif target >nums[m2]:
                l=m2+1
            else:
                l = m1+1
                r = m2-1 
        return -1
        