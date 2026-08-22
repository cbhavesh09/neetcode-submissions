class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ml,mr = 0,len(matrix)-1
        while ml<=mr:
            mid = (ml+mr)//2
            if target >= matrix[mid][0] and target <=matrix[mid][-1]:
                l,r = 0 ,len(matrix[mid])-1
                while l<=r:
                    m = (l+r)//2
                    if matrix[mid][m]== target:
                        return True
                    elif target>matrix[mid][m]:
                        l = m+1
                    else:
                        r = m-1
                return False
            elif target<matrix[mid][0]:
                mr = mid -1
            else:
                ml = mid+1
        return False
            