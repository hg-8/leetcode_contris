class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        grid=[set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                val=board[i][j]
                if val == "." :
                    continue
                gridno = (i//3)*3 + j//3
                if val in row[i] or val in col[j] or val in grid[gridno]:
                    return False
                row[i].add(val)
                col[j].add(val)
                grid[gridno].add(val)
        return True