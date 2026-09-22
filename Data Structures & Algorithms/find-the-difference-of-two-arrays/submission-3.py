class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hset1 = set(nums1)
        hset2 = set(nums2)
        return [list(hset1-hset2),list(hset2-hset1)]

        