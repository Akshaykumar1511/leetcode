import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # return math.sqrt((1**2)+(3**2))
        heap=[]
        for i in points:
            s=-math.sqrt((i[0]**2)+(i[1]**2))
            if len(heap)>k-1:
                heapq.heappushpop(heap,(s,i))
            else:
                heapq.heappush(heap,(s,i))
        return [i[1] for i in heap]