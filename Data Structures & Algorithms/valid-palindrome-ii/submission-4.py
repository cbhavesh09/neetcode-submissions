class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l<=r:
            if s[l]!=s[r]:
                return self.checkPalindrome(s[l+1:r+1]) or self.checkPalindrome(s[l:r])
            l+=1
            r-=1
        return True
    
    def checkPalindrome(self,arr):
        l,r = 0, len(arr)-1
        while l<=r:
            if arr[l]!=arr[r]:
                return False
            l+=1
            r-=1
        return True
        