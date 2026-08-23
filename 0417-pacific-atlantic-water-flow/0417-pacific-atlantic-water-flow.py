from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n,m=len(heights),len(heights[0])
        p_que,p_seen=deque(),set()
        a_que,a_seen=deque(),set()

        for i in range(m):
            p_que.append((0,i))
            p_seen.add((0,i))
        for j in range(1,n):
            p_que.append((j,0))
            p_seen.add((j,0))
        for i in range(m):
            a_que.append((n-1,i))
            a_seen.add((n-1,i))
        for j in range(n-1):
            a_que.append((j,m-1))
            a_seen.add((j,m-1))

        def get_cords(que,seen):
            while que:
                i,j=que.popleft()
                for a,h in ((0,1),(1,0),(0,-1),(-1,0)):
                    r,c=i+a,j+h
                    if 0<=r<n and 0<=c<m and heights[r][c]>=heights[i][j] and (r,c) not in seen:
                        seen.add((r,c))
                        que.append((r,c))

        get_cords(p_que,p_seen)
        get_cords(a_que,a_seen)
        return list(p_seen.intersection(a_seen))