class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        tcounter = counter = 0
        for num in nums:
            if num -1 not in hset:
                tcounter = 1
                while num+tcounter in hset:
                    tcounter +=1
                counter = max(tcounter,counter)
        return counter
        