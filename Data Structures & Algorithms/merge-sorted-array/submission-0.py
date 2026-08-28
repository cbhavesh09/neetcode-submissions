class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = -n
        while k<=-1:
            nums1.pop()
            k+=1
        nums1.extend(nums2)
        for i in range(m,m+n):
            key = nums1[i]
            j = i-1
            while j>=0 and nums1[j]>key:
                nums1[j+1]=nums1[j]
                j-=1
            nums1[j+1]= key 



        