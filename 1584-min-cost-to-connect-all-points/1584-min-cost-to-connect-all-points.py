import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #prims algo
        n=len(points)
        seen=set()
        heap=[(0,0)]
        ans=0
        while len(seen)<n:
            dist,i=heapq.heappop(heap)
            if i in seen:
                continue
            seen.add(i)
            ans+=dist
            xi,yi=points[i]
            for j in range(n):
                if j not in seen:
                    xj,yj=points[j]
                    d=abs(xi-xj)+abs(yi-yj)
                    heapq.heappush(heap,(d,j))
        return ans