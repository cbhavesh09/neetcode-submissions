class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        fa = []
        p1= p2 = 0
        while p1<len(nums1)and p2<len(nums2):
            if nums1[p1]<nums2[p2]:
                fa.append(nums1[p1])
                p1+=1
            else:
                fa.append(nums2[p2])
                p2+=1
        if p1<len(nums1):
            fa.extend(nums1[p1:])
        if p2<len(nums2):
            fa.extend(nums2[p2:])
        n = len(fa)
        m = n//2
        if n%2==0:
            ans = (fa[m]+fa[m-1])/2
            return ans
        else:
            return fa[m]
        