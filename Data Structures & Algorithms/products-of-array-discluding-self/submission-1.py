class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr = []
        ps = []

        postfix = 1
        prefix = 1

        for x in nums:
            pr.append(prefix)
            prefix *= x
        
        for y in range(len(nums)-1,-1,-1):
            postfix*=nums[y]
            ps.append(postfix)
        ps.pop()
        ps = ps[::-1]
        for num in range(len(ps)):
            pr[num] =ps[num]* pr[num]
        return pr


        