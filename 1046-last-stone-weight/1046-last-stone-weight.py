import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for i in range(len(stones)):
            heapq.heappush(heap,-stones[i])
        while len(heap)>1:
            min1,min2=heapq.heappop(heap),heapq.heappop(heap)
            if min1!=min2:
                heapq.heappush(heap,min1-min2)
        return -heap[0] if heap else 0