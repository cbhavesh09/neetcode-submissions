class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for num in matrix:
            if num[-1]>=target:
                if num[-1]==target:
                    return True
                else:
                    l,r = 0 , len(num)-1
                    while l<=r:
                        mid = (l+r)//2
                        if target == num[mid]:
                            return True
                        elif target >num[mid]:
                            l = mid+1
                        else:
                            r = mid -1
                    return False
        return False
            
        