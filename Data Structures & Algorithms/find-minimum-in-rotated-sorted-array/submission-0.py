class Solution:
    def findMin(self, nums: List[int]) -> int:
        kmin = nums[0]
        for num in nums:
            if num<kmin:
                kmin = num
        return kmin