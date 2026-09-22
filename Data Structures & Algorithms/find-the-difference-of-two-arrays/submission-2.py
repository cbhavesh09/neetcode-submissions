class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hset1 = set(nums1)
        hset2 = set(nums2)
        ans = [[],[]]
        for num in hset1:
            if num not in hset2:
                ans[0].append(num)
        for num in hset2:
            if num not in hset1:
                ans[1].append(num)
        return ans

        