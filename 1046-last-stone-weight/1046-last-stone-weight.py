import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone=[0]*len(stones)
        for i in range(len(stones)):
            stone[i]=-stones[i]
        heapq.heapify(stone)
        while len(stone)>1:
            min1=heapq.heappop(stone)
            min2=heapq.heappop(stone)
            if min1==min2:
                continue
            else:
                heapq.heappush(stone,min1-min2)
        return abs(stone[0]) if stone else 0