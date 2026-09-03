class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums)%2 !=0:
            return False
        hset = {}
        for num in nums:
            hset[num]= 1+ hset.get(num,0)
        for fre in hset.values():
            if fre%2!=0:
                return False
        return True

            
        