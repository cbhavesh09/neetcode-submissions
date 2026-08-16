class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hset = {}
        bucket = [[] for n in range(len(nums)+1)]
        for num in nums:
            hset[num]= 1+ hset.get(num,0)
        for n,c in hset.items():
            bucket[c].append(n)
        ans = []
        for num in range(len(bucket)-1,-1,-1):
            if not bucket[num]:
                continue
            for x in bucket[num]:
                if len(ans)==k:
                    return ans
                ans.append(x)
        return ans     

            
        
        