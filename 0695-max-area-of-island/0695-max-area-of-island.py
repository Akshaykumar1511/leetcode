class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def back(i,j):
            if i>=n or j>=m or i<0 or j<0 or grid[i][j]==0:
                return 0
            grid[i][j]=0
            return 1+back(i+1,j)+back(i-1,j)+back(i,j+1)+back(i,j-1)
        n,m=len(grid),len(grid[0])
        maxx=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    maxx=max(back(i,j),maxx)
        return maxx