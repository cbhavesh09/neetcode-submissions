class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        longest = 0
        for num in nums:
            length = 0
            if num-1 not in hset:
                while num+length in hset:
                    length+=1
                longest = max(length,longest)
        return longest

        