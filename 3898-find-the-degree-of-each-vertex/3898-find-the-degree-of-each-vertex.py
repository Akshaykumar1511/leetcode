class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        res=[0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==1:
                    res[j]+=1
        return res
