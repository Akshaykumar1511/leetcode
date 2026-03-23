class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof=0
        minval=float('inf')
        for i in prices:
            if i < minval:
                minval=i
            prof=i-minval
            if prof>maxprof:
                maxprof=prof
        return maxprof