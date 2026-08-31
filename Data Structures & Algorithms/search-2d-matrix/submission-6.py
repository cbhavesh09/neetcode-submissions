class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l1, r1 = 0, len(matrix) - 1

        # Binary search for the correct row
        while l1 <= r1:

            m1 = (l1 + r1) // 2

            if target < matrix[m1][0]:
                r1 = m1 - 1

            elif target > matrix[m1][-1]:
                l1 = m1 + 1

            else:
                # Binary search inside the row
                l, r = 0, len(matrix[m1]) - 1

                while l <= r:
                    m = (l + r) // 2

                    if target == matrix[m1][m]:
                        return True

                    elif target < matrix[m1][m]:
                        r = m - 1

                    else:
                        l = m + 1

                return False

        return False