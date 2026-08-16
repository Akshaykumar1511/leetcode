class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r,c=len(grid),len(grid[0])
        island=0
        def rec(i,j):
            if i<0 or i>=r or j<0 or j>=c or grid[i][j]=="0":
                return
            else:
                grid[i][j]="0"
                rec(i+1,j)
                rec(i-1,j)
                rec(i,j+1)
                rec(i,j-1)                
        for i in range(r):
            for j in range(c):
                if grid[i][j]=="1":
                    island+=1
                    grid[i][j]=="0"
                    rec(i,j)
        return island