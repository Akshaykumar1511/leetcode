class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        l,r=0,(m*n)-1
        while l<=r:
            M=(l+r)//2
            i,j=M//n,M%n
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target:
                l=M+1
            else:
                r=M-1
        else:
            return False