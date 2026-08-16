class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hmap = []
        for x in nums:
            if x in hmap:
                hmap.remove(x)
            else:
                hmap.append(x)
        return hmap[0]



        
            

        