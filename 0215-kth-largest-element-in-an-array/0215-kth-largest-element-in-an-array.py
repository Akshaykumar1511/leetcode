import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)
        num=[0]*n
        for i in range(n):
            num[i]=-nums[i]
        heapq.heapify(num)
        for i in range(k-1):
            heapq.heappop(num)
        return -num[0]