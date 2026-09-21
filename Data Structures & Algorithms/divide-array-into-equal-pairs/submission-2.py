class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hset = {}
        for num in nums:
            hset[num] = 1+hset.get(num,0)
        for freq in hset.values():
            if freq %2!=0:
                return False
        return True
            

        


        