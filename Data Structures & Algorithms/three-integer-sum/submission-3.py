class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        fa = []
        for i in range(len(nums)):
            r = len(nums)-1
            l = i+1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    fa.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l-1]== nums[l]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
                elif nums[i]+nums[l]+nums[r]>0:
                    r-=1
                else:
                    l+=1
        return fa




        