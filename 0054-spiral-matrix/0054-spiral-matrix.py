class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        ans=[]
        direction=0
        top=0
        bottom=m-1
        left=0
        right=n-1
        while top<=bottom and left<=right:
            if direction==0:
                for j in range(left,right+1):
                    ans.append(matrix[top][j])
                top+=1
                direction=1
            elif direction==1:
                for i in range(top,bottom+1):
                    ans.append(matrix[i][right])
                right-=1
                direction=2
            elif direction==2:
                for j in range(right,left-1,-1):
                    ans.append(matrix[bottom][j])
                bottom-=1
                direction=3
            elif direction==3:
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                left+=1
                direction=0
        return ans 

            