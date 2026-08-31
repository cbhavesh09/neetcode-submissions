class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        if target <nums[l]:
            return 0
        elif target >nums[r]:
            return r+1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]== target:
                return mid
            elif target <nums[mid]:
                r = mid-1
            else:
                l = mid+1
        if target > nums[mid]:
            return mid+1
        else:
            return mid
        
        