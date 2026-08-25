from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY,FRESH,ROTTEN=0,1,2
        d=deque()
        fo=0
        n,m=len(grid),len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==FRESH:
                    fo+=1
                elif grid[i][j]==ROTTEN:
                    d.append((i,j))
        if fo==0:
            return 0
        mo=-1
        while d:
            l=len(d)
            mo+=1
            for _ in range(l):
                i,j=d.popleft()
                for r,c in ((i,j+1),(i,j-1),(i-1,j),(i+1,j)):
                    if 0<=r<n and 0<=c<m and grid[r][c]==FRESH:
                        d.append((r,c))
                        grid[r][c]=ROTTEN
                        fo-=1
        if fo==0:
            return mo
        else:
            return -1