class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hset1 = [set() for _ in range(9)]
        hset2 = [set()for _ in range(9)]
        hset3 = [set() for _ in range(9)]

        for rows in range(9):
            for cols in range(9):
                if board[rows][cols]=='.':
                    continue
                if board[rows][cols] in hset1[rows] or board[rows][cols] in hset2[cols] or board[rows][cols] in hset3[(rows//3)*3 + (cols//3)]:
                    return False
                hset1[rows].add(board[rows][cols])
                hset2[cols].add(board[rows][cols])
                hset3[(rows//3)*3+ (cols//3)].add(board[rows][cols])
        return True
        