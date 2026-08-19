class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def back(i,j):
            if i<0 or i>=n or j<0 or j>=m or grid[i][j]=="0":
                return
            grid[i][j]="0"
            back(i+1,j)
            back(i-1,j)
            back(i,j+1)
            back(i,j-1)
        n,m=len(grid),len(grid[0])
        cnt=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    cnt+=1
                    back(i,j)
        return cnt