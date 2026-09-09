class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers)-1
        while l<=r:
            tsum = numbers[l]+numbers[r]
            if tsum == target:
                return [l+1,r+1]
            if tsum >target:
                r-=1
            else:
                l+=1

        