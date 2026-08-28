class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m-1
        lst = m+n-1
        r = n-1
        while r>=0 and l>=0:
            if nums1[l]>nums2[r]:
                nums1[lst],nums1[l]= nums1[l],nums1[lst]
                l-=1
            else:
                nums1[lst]= nums2[r]
                r-=1
            lst-=1
        while r>=0:
            nums1[lst]= nums2[r]
            lst-=1
            r-=1
        

        