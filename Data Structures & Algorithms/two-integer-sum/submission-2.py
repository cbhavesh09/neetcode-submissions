class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        harr = {}
        for i,num in enumerate(nums):
            ans = target-num
            if ans in harr:
                return [harr[ans],i]
            harr[num]=i
        

        