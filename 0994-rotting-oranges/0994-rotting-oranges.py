from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        FRESH,EMPTY,ROTTEN=1,0,2
        q=deque()
        n,m=len(grid),len(grid[0])
        minn=-1
        frec=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==FRESH:
                    frec+=1
                if grid[i][j]==ROTTEN:
                    q.append((i,j))
        if frec==0:
            return 0
        while q:
            lenq=len(q)
            minn+=1
            for _ in range(lenq):
                i,j=q.popleft()
                for r,c in ((i+1,j),(i-1,j),(i,j-1),(i,j+1)):
                    if 0<=r<n and 0<=c<m and grid[r][c]==FRESH:
                        q.append((r,c))
                        frec-=1
                        grid[r][c]=ROTTEN
        if frec==0:
            return minn
        else:
            return -1