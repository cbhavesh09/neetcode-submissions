class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        innum1= []
        innum2 = []
        for num in nums1:
            if num not in nums2:
                if num not in innum2:
                    innum2.append(num)
        for num in nums2:
            if num not in nums1:
                if num not in innum1:
                    innum1.append(num)
        return [innum2,innum1]