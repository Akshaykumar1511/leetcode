import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        s=defaultdict(list)
        for i in times:
            s[i[0]].append((i[1],i[2]))
        heap=[(0,k)]
        seen={}
        while heap:
            dist,node=heapq.heappop(heap)
            if node in seen:
                continue
            seen[node]=dist
            for nei in s[node]:
                next_nei,dist=nei
                heapq.heappush(heap,(dist+seen[node],next_nei))
        return max(seen.values()) if len(seen)==n else -1