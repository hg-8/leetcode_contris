class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        zero_rows=set()
        zero_cols=set()

        for rowno,row in enumerate(matrix):
            for colno,element in enumerate(row):
                if element ==0:
                    zero_rows.add(rowno)
                    zero_cols.add(colno)
        for r in zero_rows:
            for c in range(n):
                matrix[r][c]=0
        for c in zero_cols:
            for r in range(m):
                matrix[r][c]=0
        return matrix
        
        