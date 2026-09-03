class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            h1 = set()
            for num in row:
                if num == '.':
                    continue
                if num in h1:
                    return False
                h1.add(num)
        for num in range(9):
            h2 = set()
            for col in range(9):
                if board[col][num]=='.':
                    continue
                if board[col][num] in h2:
                    return False
                h2.add(board[col][num])
        for rows in range(0,9,3):
            for col in range(0,9,3):
                h3 = set()
                for i in range(rows,rows+3):
                    for j in range(col,col+3):
                        if board[i][j]=='.':
                            continue
                        if board[i][j] in h3:
                            return False
                        h3.add(board[i][j])
        return True



        