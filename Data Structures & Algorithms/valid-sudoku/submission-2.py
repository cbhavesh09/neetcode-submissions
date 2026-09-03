class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        h1 = [set() for _ in range(9)]
        h2 = [set() for _ in range(9)]
        h3 = [set() for _ in range(9)]

        for rows in range(9):
            for cols in range(9):
                if board[rows][cols]== '.':
                    continue
                if board[rows][cols] in h1[rows] or board[rows][cols] in h2[cols] or board[rows][cols] in h3[(rows//3)*3 + (cols//3)]:
                    return False
                h1[rows].add(board[rows][cols])
                h2[cols].add(board[rows][cols])
                h3[(rows//3)*3+(cols//3)].add(board[rows][cols])
        return True


        