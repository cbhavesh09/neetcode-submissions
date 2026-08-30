class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0]*2*len(nums)
        for num in range(len(nums)):
            ans[num]= nums[num]
            ans[num+len(nums)]= nums[num]
        return ans
        