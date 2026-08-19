class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        best=0
        def back(i,j):
            if i<0 or i>=n or j<0 or j>=m or grid[i][j]==0:
                return 0
            grid[i][j]=0
            below=back(i+1,j)
            right=back(i,j+1)
            up=back(i-1,j)
            left=back(i,j-1)
            return 1+below+right+left+up

        n,m=len(grid),len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    cnt=back(i,j)
                    best=max(cnt,best)
        return best