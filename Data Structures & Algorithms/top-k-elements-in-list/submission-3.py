class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        hset = {}
        fr = []
        for num in nums:
            hset[num] = 1+ hset.get(num,0)
        for num in hset:
            buckets[hset[num]].append(num)
        
        for num in range(len(buckets)-1,-1,-1):
            if not buckets[num]:
                continue
            if len(fr)<k:
                for n in buckets[num]:
                    if len(fr)<k:
                        fr.append(n)
                    else:
                        return fr
        return fr
            
        