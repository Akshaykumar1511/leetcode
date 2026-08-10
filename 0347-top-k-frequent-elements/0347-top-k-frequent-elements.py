import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        heap=[]
        for i,v in counter.items():
            heapq.heappush(heap,(v,i))
        for _ in range(len(heap)-k):
            heapq.heappop(heap)
        return [h[1] for h in heap]